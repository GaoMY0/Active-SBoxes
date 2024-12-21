
def printresult(result,X,L,Y,S,rounds,M):
    f=open("R_trail"+str(M)+".txt", "a")
    for r in range(rounds):
        if r!=0:#输出X
            for y in range(3):
                for z in range(32):
                    for x in range(4):
                        if result[X[r][x][y][z]] > 0:
                            f.write("1")
                        else:
                            f.write(".")
                    f.write(" ")
                f.write("\n")
            # PL操作
            for i in range(160):
                f.write("-")
            f.write("PL\n")

            for y in range(3):
                for z in range(32):
                    for x in range(4):
                        if result[L[r][x][y][z]] > 0:
                            f.write("1")
                        else:
                            f.write(".")
                    f.write(" ")
                f.write("\n")
            # West操作
            for i in range(160):
                f.write("-")
            f.write("West\n")

            for y in range(3):
                for z in range(32):
                    for x in range(4):
                        if result[Y[r][x][y][z]]>0:
                            f.write("1")
                        else:
                            f.write(".")
                    f.write(" ")
                f.write("\n")
            # PS操作
            for i in range(160):
                f.write("-")
            f.write("PS\n")

        if r!=rounds-1:
            for y in range(3):
                for z in range(32):
                    for x in range(4):
                        if result[S[r][x][y][z]]>0:
                            f.write("1")
                        else:
                            f.write(".")
                    f.write(" ")
                f.write("\n")
            # East操作
            for i in range(160):
                f.write("-")
            f.write("East\n")

    f.write("\n")
    f.close()


