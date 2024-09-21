import face_recognition


class ImageHelper:

    staticmethod
    def face_detector_helper(user_face, input_face_image):
        user_image = face_recognition.load_image_file(user_face)
        input_image = face_recognition.load_image_file(input_face_image)

        user_encoding = face_recognition.face_encodings(user_image)[0]
        input_encoding = face_recognition.face_encodings(input_image)[0]

        results = face_recognition.compare_faces([user_encoding], input_encoding)
        return results[0]
