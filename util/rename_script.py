import os
import glob

def rename_bottts_images(directory):
    # 匹配 bottts 开头的 jpg 文件
    pattern = os.path.join(directory, "bottts*.jpg")
    files = glob.glob(pattern)

    # 按文件修改时间排序
    files.sort(key=os.path.getmtime)

    # 重命名文件
    for i, filepath in enumerate(files, start=1):
        new_name = f"avatar-{i}.jpg"
        new_path = os.path.join(directory, new_name)

        # 防止覆盖已有文件
        if os.path.exists(new_path):
            print(f"跳过 {new_path}，已存在。")
            continue

        os.rename(filepath, new_path)
        print(f"已重命名：{os.path.basename(filepath)} -> {new_name}")

if __name__ == "__main__":
    target_dir = input("请输入目标目录路径：").strip()
    if not os.path.isdir(target_dir):
        print("❌ 输入的目录不存在，请检查路径。")
    else:
        rename_bottts_images(target_dir)
