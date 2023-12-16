import TTS
import STT
import subtitles

if __name__ == "__main__":
    TTS.TTS("""
        On a stormy night, atop a craggy cliff, stood an old lighthouse, its beam piercing through the fog. Inside, an elderly keeper named Elias tended to the flame. Unknown to most, Elias held a secret: he could speak with the sea. Each night, the waves would tell him tales of lost ships and hidden treasures.

        That night, amid the roar of thunder, the sea whispered of a ship in peril, struggling against the relentless storm. Guided by Elias' light, the ship found safe passage. As dawn broke, the grateful captain visited the lighthouse, offering a weathered, ancient map as thanks.

        Elias, with a twinkle in his eye, realized the adventure he'd longed for had just begun. Hidden in the map's intricate lines lay the path to a legendary island, a place of forgotten magic. And so, with the map in hand and the sea as his guide, Elias set sail towards a new horizon, ready to uncover the mysteries that awaited.    
    In a quaint village nestled among rolling hills and vibrant meadows, there lived a young artist named Elara. Her small studio was filled with canvases of all sizes, each one bursting with color and life. Elara's special talent was painting the dreams of the villagers. They would come to her with fragments of their dreams, and she would transform these wisps of imagination into vivid paintings.

One evening, as the sun dipped below the horizon, casting a golden glow over the village, a mysterious old man visited Elara. He spoke of a dream unlike any other, a dream of a hidden valley where the stars touched the earth and the air shimmered with magic. His description was faint and hazy, but Elara felt a surge of inspiration.

For days, she worked tirelessly, her brushes dancing across the canvas, trying to capture the essence of the dream. But no matter how hard she tried, the painting felt incomplete. Frustrated and weary, Elara decided to seek out the valley herself, believing that seeing it would help her complete the masterpiece.

She embarked on a journey through unknown lands, guided by the stars and the old man's descriptions. After several days, deep in a forgotten corner of the world, Elara found the valley. It was more breathtaking than she had imagined: a tranquil oasis bathed in starlight, with flowers that glowed softly and a gentle river that sang a melodious tune.

Under the starlit sky, Elara painted with newfound passion, her brush capturing the enchanting beauty of the valley. When she returned to the village, her painting was hailed as her greatest masterpiece, a mesmerizing blend of dream and reality that captivated all who saw it.

The painting of the star-touched valley not only brought joy to the villagers but also inspired them to follow their dreams, no matter how elusive they seemed. And as for Elara, she continued to paint, her art forever touched by the magic of the valley where the stars met the earth.
    """, "test")
    STT.STS("test")
    subtitles.srtFile("test")
    STT.STT(r"A:\Projects\AiShorts\test\audio.wav")