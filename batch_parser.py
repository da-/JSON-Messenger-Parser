import os
import subprocess


def run_parser():
    # update these paths to match your own
    base_input_dir  = "../your_facebook_activity/messages"
    stickers_dir    = "../your_facebook_activity/messages/stickers_used"
    base_output_dir = "../out"
    main_exec       = "./main.py"

    # name of the owner of the messages
    name = "User Name"

    for subdir in ["archived_threads", "e2ee_cutover", "filtered_threads", "inbox"]:
        input_dir = os.path.join(base_input_dir, subdir)
        for item in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item)
            if os.path.isdir(item_path):
                output_file = f"{base_output_dir}/{subdir}_{item}.html"
                subprocess.run([
                    "python3", main_exec, 
                    "-i", f"{item_path}/", 
                    "-n", name, 
                    "-o", output_file, 
                    "-s", f"{stickers_dir}/"
                ])

if __name__ == "__main__":
    run_parser()