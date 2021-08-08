# If you want to extend touple unpacking following can be used
# safe if out of bounds, gotcha make sure all unpack data fits in memory(RAM)

sample_rate, n_channel, *audio = [16000, 2, 0.43, 4.41, 0.44]

print(sample_rate, n_channel, audio)
# 16000 2 [0.43, 4.41, 0.44]


# * can be at any place, here is one gotcha
v1, *v2, v3 = [1, 2]

print(v1, v2, v3)
# 1 [] 2