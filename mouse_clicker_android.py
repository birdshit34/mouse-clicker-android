#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.config import Config
import threading
import time

# 在安卓设备上，我们使用屏幕触摸而不是鼠标点击
# 你可以根据需要修改这部分逻辑
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class AndroidClickerApp(App):
    def build(self):
        self.clicking = False
        self.click_thread = None
        
        # 主布局
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # 标题
        title = Label(
            text='手机屏幕点击器',
            size_hint_y=0.15,
            font_size=24,
            bold=True
        )
        layout.add_widget(title)
        
        # 坐标输入区域
        coord_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        
        # X坐标
        self.x_input = TextInput(
            hint_text='X坐标',
            size_hint_x=0.4,
            multiline=False,
            input_filter='int'
        )
        coord_layout.add_widget(self.x_input)
        
        # Y坐标
        self.y_input = TextInput(
            hint_text='Y坐标', 
            size_hint_x=0.4,
            multiline=False,
            input_filter='int'
        )
        coord_layout.add_widget(self.y_input)
        
        layout.add_widget(coord_layout)
        
        # 设置区域
        settings_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=0.25)
        
        # 时间间隔
        interval_layout = BoxLayout(orientation='horizontal', spacing=10)
        interval_layout.add_widget(Label(text='间隔(秒):', size_hint_x=0.4))
        self.interval_input = TextInput(
            text='1.0',
            size_hint_x=0.6,
            multiline=False,
            input_filter='float'
        )
        interval_layout.add_widget(self.interval_input)
        settings_layout.add_widget(interval_layout)
        
        # 点击次数
        count_layout = BoxLayout(orientation='horizontal', spacing=10)
        count_layout.add_widget(Label(text='次数(0=无限):', size_hint_x=0.5))
        self.count_input = TextInput(
            text='10',
            size_hint_x=0.5,
            multiline=False,
            input_filter='int'
        )
        count_layout.add_widget(self.count_input)
        settings_layout.add_widget(count_layout)
        
        layout.add_widget(settings_layout)
        
        # 控制按钮
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=0.15)
        
        self.start_btn = Button(
            text='开始点击',
            background_color=(0, 1, 0, 1),
            font_size=18,
            size_hint_x=0.5
        )
        self.start_btn.bind(on_press=self.start_clicking)
        button_layout.add_widget(self.start_btn)
        
        self.stop_btn = Button(
            text='停止点击',
            background_color=(1, 0, 0, 1),
            font_size=18,
            size_hint_x=0.5,
            disabled=True
        )
        self.stop_btn.bind(on_press=self.stop_clicking)
        button_layout.add_widget(self.stop_btn)
        
        layout.add_widget(button_layout)
        
        # 状态显示
        self.status_label = Label(
            text='状态: 等待开始',
            size_hint_y=0.15,
            font_size=18,
            color=(1, 1, 0, 1)
        )
        layout.add_widget(self.status_label)
        
        # 使用说明
        help_text = (
            '使用说明:\n'
            '1. 输入目标坐标X,Y\n'
            '2. 设置点击间隔时间\n'
            '3. 设置点击次数\n'
            '4. 点击"开始点击"\n'
            '5. 可随时点击"停止"\n'
            '提示: 在安卓上运行时'
            '需要有悬浮窗权限'
        )
        help_label = Label(
            text=help_text,
            size_hint_y=0.2,
            font_size=14,
            color=(0, 1, 1, 1)
        )
        layout.add_widget(help_label)
        
        return layout
    
    def validate_inputs(self):
        """验证输入"""
        try:
            x = int(self.x_input.text) if self.x_input.text else 0
            y = int(self.y_input.text) if self.y_input.text else 0
            interval = float(self.interval_input.text) if self.interval_input.text else 1.0
            count = int(self.count_input.text) if self.count_input.text else 10
            
            if x < 0 or y < 0:
                self.show_popup("错误", "坐标不能为负数")
                return False
                
            if interval <= 0:
                self.show_popup("错误", "间隔时间必须大于0")
                return False
                
            return True
            
        except ValueError:
            self.show_popup("错误", "请输入有效的数字")
            return False
    
    def show_popup(self, title, message):
        """显示提示窗口"""
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def start_clicking(self, instance):
        """开始点击"""
        if not self.validate_inputs():
            return
            
        if self.clicking:
            return
            
        self.clicking = True
        self.start_btn.disabled = True
        self.stop_btn.disabled = False
        self.status_label.text = "状态: 正在点击..."
        self.status_label.color = (0, 1, 0, 1)
        
        # 创建点击线程
        self.click_thread = threading.Thread(target=self.click_loop, daemon=True)
        self.click_thread.start()
    
    def click_loop(self):
        """点击循环"""
        try:
            x = int(self.x_input.text) if self.x_input.text else 0
            y = int(self.y_input.text) if self.y_input.text else 0
            interval = float(self.interval_input.text) if self.interval_input.text else 1.0
            count = int(self.count_input.text) if self.count_input.text else 10
            
            click_count = 0
            
            while self.clicking:
                if count > 0 and click_count >= count:
                    break
                
                # 在安卓上，这个需要改为实际的触摸事件
                # 这里只是模拟逻辑
                Clock.schedule_once(lambda dt, c=click_count: self.update_status(c), 0)
                click_count += 1
                
                for _ in range(int(interval * 10)):
                    if not self.clicking:
                        break
                    time.sleep(0.1)
            
            Clock.schedule_once(lambda dt: self.on_clicking_finished(), 0)
            
        except Exception as e:
            Clock.schedule_once(lambda dt: self.show_popup("错误", f"点击时出错: {e}"), 0)
            Clock.schedule_once(lambda dt: self.stop_clicking(), 0)
    
    def update_status(self, count):
        """更新状态"""
        self.status_label.text = f"状态: 正在点击 (已点击: {count} 次)"
    
    def on_clicking_finished(self):
        """点击完成"""
        self.stop_clicking()
        if self.clicking:
            self.show_popup("完成", f"点击已完成! 总共点击了 {int(self.count_input.text or '0')} 次")
    
    def stop_clicking(self, instance=None):
        """停止点击"""
        self.clicking = False
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.status_label.text = "状态: 已停止"
        self.status_label.color = (1, 1, 0, 1)

if __name__ == "__main__":
    AndroidClickerApp().run()