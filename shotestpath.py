
# MODULE IMPORTS
from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
import os

# INITIAL LIST FOR EDGE VERTEX DATA
e =[]
lo =[]
lo2 = []

# THE MAIN TKINTER GUI 
def home():
    top = Tk()
    top.geometry("600x400+380+160")
    top.resizable(False,False)
    top.title("Shortest path")
    top.configure(background="olive")
    top.counter = 0 # VERTEX COUNTER
    top.count = 0   # ERROR COUNTER

    # CLEAR AND RESET
    def clr():
        plt.close('all')
        top.destroy()
        os.startfile("shotestpath.py")
        os.close("shotestpath.py")
        main()
    
    # ERROR MODULE
    def error():
        top.count +=1
        er = Label(top, text="ERROR !! FILL THE INPUT CORRECTLY "+ str(top.count), font=("Helvetica", 12, "bold"), fg="maroon", bg="Olive")
        er.place(x=2, y=2)

    # VISUALIZING THE GRAPH
    def grapho():
        plt.clf()
        pos = nx.spring_layout(G)
        path = len(pro)
        edge =[]
        for j in range(path-1):
            temp =[]
            temp.append(pro[j])
            temp.append(pro[j+1])
            edge.append(temp)
        label ={}
        lo1 =[]
        for l in range (len(lo)):
            lo1.append(lo[l][0])
        for k in range(len(lo)):
            label[lo1[k]] = lo2[k]
        nx.draw(G, pos, node_color= 'grey',edge_color ='grey',with_labels=True)
        nx.draw_networkx_edges(G,pos,edgelist=edge,edge_color='red',arrowsize=50)
        nx.draw_networkx_nodes(G,pos,nodelist=pro,node_color='red')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=label ,font_color='Blue')
        plt.show()
        
    # PATH CALCULATION
    def result(e):
        ee5 = e5.get()
        e5.delete(0,END)
        ee6 = e6.get()
        e6.delete(0,END)
        if ee5 =='' or ee5.isdigit() or ee6 =='' or ee6.isdigit():
            error()
        else:
            global G
            G = nx.DiGraph()
            G.add_weighted_edges_from(e)
            global pro
            pro = nx.dijkstra_path(G,ee5,ee6)
            t111 = Label(top, text="THE RESULTANT SHORTEST PATH IS:", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t111.place(x=10, y=320)
            t111 = Label(top, text= str(pro).replace(',','->'), font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t111.place(x=10, y=350)

            btn4  = Button(top,text="VISUALIZE",width=10,bg="turquoise",bd=5, command=grapho)
            btn4.place(x=400,y=360)

    # POINT TOWARDS RESULTS
    def postulate():
        result(e)
    
    # TAKING INPUTS FOR THE SOURCE AND DESTINATION TO FIND OUT PATH
    def chetos():
            t11 = Label(top, text="INPUT THE SOURCE AND DESTINATION BETWEEN\n WHICH YOU ARE FINDING THE SHORTEST PATH", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t11.place(x=10, y=200)

            t5 = Label(top, text="SOURCE:", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t5.place(x=20, y=270)

            global e5
            e5=Entry(top,bd=5, width='10')
            e5.place(x=120,y=270)

            t6 = Label(top, text="DESTINATION:", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t6.place(x=220, y=270)

            global e6
            e6=Entry(top,bd=5, width='10')
            e6.place(x=370,y=270)

            btn3  = Button(top,text="CALCULATE",width=10,bg="turquoise",bd=5, command=postulate)
            btn3.place(x=480,y=270)

    # APPENDING THE EDGES, VERTICES AND THEIR RESPECTIVE COST OR WEIGHT TO THE GRSPH LIST
    def destiny():
        ee2 = e2.get()
        e2.delete(0,END)
        ee3 = e3.get()
        e3.delete(0,END)
        ee4 = e4.get()
        e4.delete(0,END)
        if ee2 =='' or ee2.isdigit() or ee3 =='' or ee3.isdigit() or ee4 =='' or ee4 =='0' or ee4.isalpha():
            error()
        else:
            list =[]
            list1 =[]
            list2 =[]
            a1 = ee2
            a2 = ee3
            a3 = int(ee4)
            list.append(a1)
            list.append(a2)
            list1.append((a1,a2))
            list.append(a3)
            list2.append(a3)
            lo.append(list1)
            string2 = str(list2).replace('[', '').replace(']', '')
            e.append(list)
            lo2.append(string2)
            top.counter +=1
            if top.counter == ee1:
                chetos()
            
    # TAKING THE INPUT FOR EACH EDGE VERTEX AND THEIR RESPECTIVE COST
    def edges():
        eex = e1.get()
        e1.delete(0,END)
        if eex == '' or eex == '0' or eex.isalpha():
            error()
        else:
            global ee1
            ee1 = int(eex)
            t1 = Label(top, text="FILL ALL THE "+str(ee1)+" VERTEX-EDGE DETAILS", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t1.place(x=40, y=120)

            t2 = Label(top, text="FROM:", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t2.place(x=20, y=150)

            global e2
            e2=Entry(top,bd=5, width='10')
            e2.place(x=100,y=150)
       

            t3 = Label(top, text="TO:", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t3.place(x=200, y=150)
        
            global e3
            e3=Entry(top,bd=5, width='10')
            e3.place(x=250,y=150)

            t4 = Label(top, text="COST:", font=("Helvetica", 15, "bold"), fg="black", bg="Olive")
            t4.place(x=350, y=150)

            global e4
            e4=Entry(top,bd=5, width='10')
            e4.place(x=430,y=150)

            btn2  = Button(top,text="NEXT",width=5,bg="turquoise",bd=5, command=destiny)
            btn2.place(x=530,y=150)
        
    tittle1 = Label(top, text="FINDING SHORTEST DISTANCE", font=("Helvetica", 20, "bold italic"), fg="black", bg="Olive")
    tittle1.place(x=90, y=20)

    ITEM1 =Label(top, text="ENTER NUMBER OF EDGES:", font=("Helvetica",15,'bold'),fg="black",bg="olive")
    ITEM1.place(x=10, y=70)

    global e1
    e1=Entry(top,bd=5, width='10')
    e1.place(x=300,y=70)
    

    btn1  = Button(top,text="NEXT",width=5,bg="turquoise",bd=5,command=edges)
    btn1.place(x=400,y=68)

    btn5  = Button(top,text="RESET",width=5,bg="turquoise",bd=5, command=clr)
    btn5.place(x=530,y=360)

    top.mainloop()

# JUST A LOOP THROUGH MAIN FUNCTION FOR CLEAR
def main():
    home()

main()