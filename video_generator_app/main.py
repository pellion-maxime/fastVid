import os
import cv2
import argparse
import conf  # Assurez-vous d'avoir un fichier conf.py avec la variable IMAGEMAGICK_BINARY définie
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip, ImageClip, concatenate_audioclips
import pyttsx3

# Spécifiez le chemin vers l'exécutable ImageMagick depuis conf.py
os.environ['IMAGEMAGICK_BINARY'] = conf.IMAGEMAGICK_BINARY

def generate_video(image_folder, output_video, frame_rate, text, text_size, text_color, speech_text):
    # Obtient la liste des fichiers d'images dans le dossier spécifié
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

    # Vérifiez si la liste d'images est vide
    if not images:
        print("Aucune image trouvée dans le dossier spécifié.")
        return

    # Trie les images par nom de fichier
    images.sort(key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else x)
    print(f"Images trouvées : {images}")

    # Liste pour stocker les clips vidéo individuels
    clips = []

    # Crée un clip pour chaque image avec une durée spécifiée
    for image in images:
        img_path = os.path.join(image_folder, image)
        img_clip = ImageClip(img_path).set_duration(1)  # Définit chaque image à une durée de 1 seconde
        clips.append(img_clip)

    # Combine les clips en un seul clip vidéo
    video_clip = concatenate_videoclips(clips, method="compose")

    # Définir fps pour le clip vidéo
    video_clip = video_clip.set_fps(frame_rate)

    # Vérifiez la durée du clip vidéo
    print(f"Durée de la vidéo combinée : {video_clip.duration} secondes")

    # Ajoute du texte si spécifié
    if text:
        txt_clip = TextClip(text, fontsize=text_size, color=text_color, font='Arial-Bold', method='caption')
        txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(video_clip.duration)
        video_clip = CompositeVideoClip([video_clip, txt_clip])

    # Ajoute de l'audio si spécifié
    if speech_text:
        # Génère un fichier audio temporaire
        tts = pyttsx3.init()
        tts.save_to_file(speech_text, "temp_audio.mp3")
        tts.runAndWait()

        # Charge le fichier audio
        audio_clip = AudioFileClip("temp_audio.mp3")
        
        # Ajuster la durée de l'audio pour qu'elle corresponde à la durée de la vidéo
        if audio_clip.duration < video_clip.duration:
            # Duplique l'audio jusqu'à ce qu'il atteigne la durée requise
            audio_clips = [audio_clip] * (int(video_clip.duration // audio_clip.duration) + 1)
            audio_clip = concatenate_audioclips(audio_clips).set_duration(video_clip.duration)
        
        video_clip = video_clip.set_audio(audio_clip)

    # Sauvegarde la vidéo finale avec texte et/ou audio
    video_clip.write_videofile(output_video, codec='libx264', audio_codec='aac', fps=frame_rate)

    # Supprime les fichiers temporaires
    if os.path.exists("temp_video.mp4"):
        os.remove("temp_video.mp4")
    if speech_text and os.path.exists("temp_audio.mp3"):
        os.remove("temp_audio.mp3")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate video from images with optional text and speech')
    parser.add_argument('image_folder', type=str, help='Path to the folder containing images')
    parser.add_argument('output_video', type=str, help='Path to the output video file')
    parser.add_argument('--frame_rate', type=int, default=30, help='Frame rate of the output video (default: 30)')
    parser.add_argument('--text', type=str, default='', help='Text to display on the video')
    parser.add_argument('--text_size', type=int, default=30, help='Font size of the text (default: 30)')
    parser.add_argument('--text_color', type=str, default='#FF0000', help='Color of the text in hexadecimal format (default: #FF0000)')
    parser.add_argument('--speech_text', type=str, default='', help='Speech text to add as speech in the video')

    args = parser.parse_args()

    generate_video(args.image_folder, args.output_video, args.frame_rate, args.text, args.text_size, args.text_color, args.speech_text)
