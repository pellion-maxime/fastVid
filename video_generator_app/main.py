import os
import argparse
import conf  # Assurez-vous d'avoir un fichier conf.py avec la variable IMAGEMAGICK_BINARY définie
from moviepy.editor import concatenate_videoclips, AudioFileClip, ImageClip
from datetime import datetime

# Spécifiez le chemin vers l'exécutable ImageMagick depuis conf.py
os.environ['IMAGEMAGICK_BINARY'] = conf.IMAGEMAGICK_BINARY

def generate_video(image_folder, output_folder, frame_rate, background_music):
    # Crée le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Génère un nom de fichier unique basé sur l'horodatage actuel
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_video = os.path.join(output_folder, f"output_video_{timestamp}.mp4")

    # Obtient la liste des fichiers d'images dans le dossier spécifié
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]

    # Vérifiez si la liste d'images est vide
    if not images:
        print("Aucune image trouvée dans le dossier spécifié.")
        return

    # Assurez-vous qu'il y a au moins quatre images
    if len(images) < 4:
        print("Il doit y avoir au moins quatre images dans le dossier spécifié.")
        return

    # Trie les images par nom de fichier
    images.sort(key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else x)
    print(f"Images trouvées : {images}")

    # Calculez la durée pour les trois premières images (12 secondes au total, donc 4 secondes chacune)
    duration_per_image = 4  # 12 secondes pour 3 images

    # Liste pour stocker les clips vidéo individuels
    clips = []

    # Crée un clip pour chaque des trois premières images avec une durée de 4 secondes
    for image in images[:3]:
        img_path = os.path.join(image_folder, image)
        img_clip = ImageClip(img_path).set_duration(duration_per_image)
        clips.append(img_clip)

    # Crée un clip pour la quatrième image qui dure 8 secondes (total = 20 secondes)
    last_image_path = os.path.join(image_folder, images[3])
    last_img_clip = ImageClip(last_image_path).set_duration(8)
    clips.append(last_img_clip)

    # Combine les clips en un seul clip vidéo
    video_clip = concatenate_videoclips(clips, method="compose")

    # Définir fps pour le clip vidéo
    video_clip = video_clip.set_fps(frame_rate)

    # Vérifiez la durée du clip vidéo
    print(f"Durée de la vidéo combinée : {video_clip.duration} secondes")

    # Ajoute de la musique de fond si spécifié
    if background_music:
        # Charge le fichier audio de fond
        audio_clip = AudioFileClip(background_music).subclip(0, video_clip.duration)
        
        # Ajuster la durée de l'audio pour qu'elle corresponde à la durée de la vidéo
        if audio_clip.duration < video_clip.duration:
            audio_clip = audio_clip.set_duration(video_clip.duration)
        
        video_clip = video_clip.set_audio(audio_clip)

    # Sauvegarde la vidéo finale avec audio
    video_clip.write_videofile(output_video, codec='libx264', audio_codec='aac', fps=frame_rate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate video from images with optional background music')
    parser.add_argument('image_folder', type=str, help='Path to the folder containing images')
    parser.add_argument('output_folder', type=str, help='Path to the output folder')
    parser.add_argument('--frame_rate', type=int, default=30, help='Frame rate of the output video (default: 30)')
    parser.add_argument('--background_music', type=str, default='', help='Path to the background music file')

    args = parser.parse_args()

    generate_video(args.image_folder, args.output_folder, args.frame_rate, args.background_music)
