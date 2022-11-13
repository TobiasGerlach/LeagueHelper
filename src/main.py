import cv2
from LeagueHelper.ScreenCapture import ScreenCapture
import datetime
from pathlib import Path

if __name__ == "__main__":
    while True:

        path_to_dataset = Path("E:\Bilder\Trainingsdaten_lol")
        current_time = datetime.datetime.now()
        filename = (
            str(current_time.year)
            + str(current_time.month)
            + str(current_time.day)
            + str(current_time.hour)
            + str(current_time.minute)
            + str(current_time.second)
            + str(current_time.microsecond)
            + ".png"
        )
        cv2.imwrite(str(path_to_dataset / Path(filename)), np.array(sct_img))
