# Image Converter (English Description)

Image Converter is a simple tool consisting of three scripts: `webp_to_jpg_png_converter.py`, and `image_to_webp_converter.py`. It facilitates the conversion of images between different formats efficiently.

## 1. webp_to_jpg_png_converter.py

**Description:**
This script converts images to the WebP format.

**Requirements:**
```cmd
pip install pillow
```

**Usage:**
Simply run the script and follow the prompts to convert images to WebP format.

**Exporting as Executable:**
For PyInstaller, use the following command:
```cmd
pyinstaller webp_to_jpg_png_converter.py --onefile --hidden-import os --hidden-import PIL
```

## 2. webp_to_jpg_png_converter.py
Description:
This script converts WebP images to JPG or PNG format.

Requirements:
```cmd
pip install pillow
```

Usage:
Simply run the script and follow the prompts to convert WebP images to JPG or PNG format.

Exporting as Executable:
For PyInstaller, use the following command:
```cmd
pyinstaller webp_to_jpg_png_converter.py --onefile --hidden-import os --hidden-import PIL
```

---
---
# Image Converter (한국어 설명)

이미지 변환기는 2 가지 스크립트인 `webp_to_jpg_png_converter.py`, 그리고 `image_to_webp_converter.py`로 구성된 간단한 도구입니다. 이 도구는 이미지를 효율적으로 다른 형식으로 변환하는 데 도움을 줍니다.

## 1. webp_to_jpg_png_converter.py

**설명:**
이 스크립트는 이미지를 WebP 형식으로 변환합니다.

**요구 사항:**
```cmd
pip install pillow
```

**사용 방법:**
스크립트를 실행하고 이미지를 WebP 형식으로 변환하려는 지시에 따르십시오.

**실행 파일로 내보내기:**
PyInstaller를 사용하여 다음 명령을 실행하십시오:
```cmd
pyinstaller webp_to_jpg_png_converter.py --onefile --hidden-import os --hidden-import PIL
```

## 2. webp_to_jpg_png_converter.py
**설명:**
이 스크립트는 WebP 이미지를 JPG 또는 PNG 형식으로 변환합니다.
```cmd
pip install pillow
```
**사용 방법:**
스크립트를 실행하고 WebP 이미지를 JPG 또는 PNG 형식으로 변환하려는 지시에 따르십시오.

**실행 파일로 내보내기:**
PyInstaller를 사용하여 다음 명령을 실행하십시오:
```cmd
pyinstaller image_to_webp_converter.py --onefile --hidden-import os --hidden-import PIL
```
