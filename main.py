from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from utils import *
import config
import time


def main():
    previous_time = ''
    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        while True:
            if not previous_time == get_current_time():
                current_time = get_current_time()
                previous_time = current_time
                im = generate_image(current_time)
                image = client.upload_file(im)
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(image))
                time.sleep(1)



if __name__ == '__main__':
    main()
