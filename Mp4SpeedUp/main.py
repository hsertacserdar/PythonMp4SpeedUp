import cv2

def speed_up_video(input_path, output_path, speed):
    # Video okuyucusunu başlat
    video = cv2.VideoCapture(input_path)

    # Video codec, boyut ve FPS bilgilerini al
    codec = int(video.get(cv2.CAP_PROP_FOURCC))
    size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Hızlandırılan videoyu yazacağımız video yazıcıyı başlat
    writer = cv2.VideoWriter(output_path, codec, fps / (1/speed), size)

    while True:
        # Bir frame oku
        ret, frame = video.read()

        if not ret:
            break

        # Frame'i hızlandır ve yazıcıya yaz
        writer.write(frame)

    # Video okuyucusunu ve yazıcıyı serbest bırak
    video.release()
    writer.release()

speed_up_video("input.mp4", "output.mp4", 64)  # Orjinal hızın iki katı hızlandırma