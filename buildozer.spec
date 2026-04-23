- name: Create buildozer.spec
  run: |
    cat > buildozer.spec << 'EOF'
[app]

title = Mouse Clicker

package.name = mouseclicker

package.domain = com.birdshit34

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

requirements = python,kivy

version = 1.0.0

[app:android]

android.permissions = SYSTEM_ALERT_WINDOW

android.api = 30

android.minapi = 21

android.ndk = 21.4.7075529

[buildozer]

log_level = 2

EOF

- name: Verify buildozer.spec created
  run: |
    echo "=== buildozer.spec content ==="
    cat buildozer.spec
