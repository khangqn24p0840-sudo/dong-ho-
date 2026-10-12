[app]
title = Dong Ho
package.name = dongho
package.domain = org.khang

source.dir = .
source.include_exts = py
source.exclude_dirs = bin,.git,.github,.buildozer

version = 0.1
requirements = python3,kivy,sdl2
orientation = portrait
fullscreen = 0

android.archs = armeabi-v7a
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
