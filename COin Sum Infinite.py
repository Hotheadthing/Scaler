A = [1, 2, 3]
B = 4
# A = [10]
# B = 10
# A = [ 2 ]
# B = 412
# A = [ 18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8 ]
# B = 458         #867621
# A = [ 406, 3, 137, 244, 46, 74, 175, 32, 506, 324, 405, 395, 298, 333, 226, 425, 552, 134, 354, 125, 472, 368, 580, 202, 449, 400, 529, 159, 68, 409, 523, 494, 515, 281, 498, 209, 578, 140, 99, 436, 194, 371, 442, 482, 591, 84, 77, 382, 484, 510, 418, 284, 398, 229, 266, 152, 212, 572, 211, 314, 302, 492, 338, 217, 113, 594, 248, 181, 45, 389, 52, 191, 561, 434, 465, 470, 238, 127, 97, 257, 399, 516, 117, 318, 236, 34, 138, 185, 445, 307, 415, 282, 116, 256, 11, 186, 239, 131, 313, 299, 565, 363, 135, 120, 543, 75, 483, 213, 489, 67, 404, 272, 263, 193, 500, 370, 495, 443, 295, 73, 568, 51, 571, 367, 20, 522, 156, 597, 459, 80, 154, 224, 1, 360, 551, 432, 258, 130, 195, 584, 455, 190, 422, 93, 62, 544, 531, 532, 124, 2, 466, 112, 123, 550, 65, 496, 366, 502, 204, 504, 177, 262, 553, 163, 44, 71, 326, 109, 215, 323, 243, 207, 512, 345, 25, 23, 421, 469, 95, 63, 55, 365, 545, 31, 556, 317, 101, 573, 270, 133, 235, 457, 320, 268, 424, 206, 335, 115, 375, 536, 566, 145, 488, 301, 30, 583, 349, 479, 280, 222, 58, 170, 208, 376, 560, 435, 12, 372, 303, 316, 267, 567, 255, 528, 420, 485, 337, 233, 198, 66, 563, 119, 304, 199, 577, 241, 85, 564, 173, 487, 339, 96, 297, 184, 401, 315, 293, 160, 475, 242, 22, 330, 90, 526, 187, 416, 540, 331, 178, 446, 89, 499, 146, 387, 19, 491, 581, 396, 452, 530, 444, 539, 250, 582, 554, 228, 392, 579, 161, 525, 555, 13, 136, 105, 569, 254, 402, 219, 76, 527, 593, 520, 341, 393, 451, 54, 165, 471, 501, 269, 513, 162, 379, 549, 453, 600, 41, 537, 381, 18, 168, 40, 88, 348, 509, 412, 237, 189, 463, 277, 141, 279, 431, 275, 352, 94, 547, 514, 419, 575, 433, 426, 264, 410, 588, 587, 172, 386, 81, 29, 259, 305, 69, 359, 144, 273, 592, 148, 390, 430, 252, 203, 14, 166, 558, 467, 598, 447, 322, 288, 511, 414, 458, 118, 142, 533, 468, 329, 110, 214, 486, 100, 438, 589, 102, 464, 407, 477, 98, 53 ]
# B = 39588

def unbounded(n,val):
    dp = [0 for i in range(B+1)]
    dp[0] = 1
    print(dp)
    for i in range(n):
        for j in range(1,B+1):
            if j >= A[i]:
                dp[j] += dp[j-A[i]]
    print(dp[B])
    # for i in range(1,n+1):
    #     for j in range(1,B+1):
    #         # print(i,j)
    #         # print(A[i-1],i)
    #         if A[i-1] <= j:
    #             dp[i][j] = (dp[i-1][j] + dp[i][j-A[i-1]]) % 1000007
    #         else:
    #             dp[i][j] = dp[i-1][j]
    # return dp[n][B] % 1000007

print(unbounded(len(A),A))



