import os
from PIL import Image

print("jpg, jpeg, png, tiff to webp converter")
print("이미지 파일(jpg, jpeg, png, tiff)을 webp 로 변환합니다\n")
print("파일이 들어있는 폴더 경로를 아래에 입력해주세요")
print("please insert folder path below:")

while True:
    upper_path = input().replace("'", "").replace('"', "")
    if os.path.isdir(upper_path):
        print("입력한 경로는 폴더 경로입니다.")
        break
    elif os.path.isfile(upper_path):
        print("입력한 경로는 파일의 경로입니다. 폴더 경로로 아래에 다시 입력해주세요:")
    else:
        print("입력한 경로가 존재하지 않거나 올바르지 않습니다. 아래에 다시 입력해주세요:")

images_list = []
for root, dirs, files in os.walk(upper_path):
    for file in files:
        file_lower = file.lower()
        if file_lower.endswith(".jpg") or file_lower.endswith(".jpeg") or file_lower.endswith(".png") or file_lower.endswith("tiff"):
            images_list.append(os.path.join(root, file))

# "result" 폴더 생성 또는 확인
result_folder = os.path.join(os.path.dirname(upper_path), "img_convert_result")

if not os.path.exists(result_folder):
    os.makedirs(result_folder)
    print(result_folder, "에 폴더를 생성했습니다.")
else:
    count = 1
    while True:
        current_folder = result_folder if count == 1 else f"img_convert_result_{count}"
        current_folder_path = os.path.join(os.path.dirname(upper_path), current_folder)
        if not os.path.exists(current_folder_path):
            os.makedirs(current_folder_path)
            print(f"{current_folder_path} 를 생성했습니다.")
            current_folder_path = result_folder
            break
        else:
            count += 1
# 모든 이미지 파일을 webp 형식으로 변환하여 "result" 폴더에 저장
origin_img_size = 0
after_img_size = 0
for image_path in images_list:
    print("")
    print(image_path, "를 처리중")
    origin_img_size += os.path.getsize(image_path)
    img = Image.open(image_path)
    new_file_path = os.path.join(result_folder, os.path.basename(image_path).split('.')[0] + ".webp")
    img.save(new_file_path, "WEBP")
    after_img_size += os.path.getsize(new_file_path)
    print(new_file_path, "가 저장되었습니다")

print("\n이미지 변환 완료되었습니다, completed.\n")
print("전체 파일 갯수: ", len(images_list))
print("변환 전 파일 용량의 합: ", origin_img_size / (1024 * 1024), "MB")
print("변환 후 파일 용량의 합: ", after_img_size / (1024 * 1024), "MB")
print("\n변환 전보다 총", (origin_img_size - after_img_size) / (1024 * 1024), "MB 가 줄어들었습니다")
