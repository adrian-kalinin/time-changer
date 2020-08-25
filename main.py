from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
import time

from utils import generate_image, delete_image, get_current_time, get_progress_of_the_day
import config


def main():
    previous_time = ''
    previous_progress_of_the_day = ''

    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        while True:
            if not previous_time == get_current_time():
                current_time = get_current_time()
                previous_time = current_time
                generate_image(current_time)
                image = client.upload_file(config.image_filename)
                client(UploadProfilePhotoRequest(image))
                client(DeletePhotosRequest([client.get_profile_photos('me')[-1]]))
                delete_image()
                time.sleep(1)

            if not previous_progress_of_the_day == get_progress_of_the_day():
                current_progress_of_the_day = get_progress_of_the_day()
                previous_progress_of_the_day = current_progress_of_the_day
                profile_bio = config.profile_bio.format(current_progress_of_the_day)
                client(UpdateProfileRequest(about=profile_bio))


if __name__ == '__main__':
    main()
