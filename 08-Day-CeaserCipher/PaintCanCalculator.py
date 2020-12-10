def paint_calc(height,width,cover):
    no_can_req = (height*width)/cover
    print(round(no_can_req))   


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


