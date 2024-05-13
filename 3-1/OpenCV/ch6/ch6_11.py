def calc_histo(image, channels, bsize, ranges):

    shape = bsize if len(channels) > 1 else (bsize[0], 1)
    hist = np.zeros(shape, np.int32)  # 히스토그램 누적 행렬

    gap = np.divide(ranges[1::2], bins) # 계급 간격

    for row in image:
        for val in row:
            idx = np.divide(val[channels], gap).astype('uint')
            hist[tuple(idx)] += 1

    return hist
