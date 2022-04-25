import Augmentor

#Put Path to Image File Here
file = Augmentor.Pipeline(r"D:\Drowning\Drowning")

file.zoom(probability=0.3, min_factor=0.8, max_factor=1.5)
file.flip_top_bottom(probability=0.4)
file.random_brightness(probability=0.3, min_factor=0.3, max_factor=1.2)
file.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
file.sample(200)

