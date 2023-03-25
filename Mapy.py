import customtkinter as ctk
import tkinter

#window
window = ctk.CTk()
window.title('Mapy')
window.geometry("1375x850")
#window.wm_resizable(False, False)

#calculate here

#calculate percentage
def Calculate_percentage(one, two, three):
    Answer = 'Answer: ' + str(round(float(one) / float(two) * 100, int(three))) + '%'
    percent_cal_answer.configure(text=Answer)

#calculate with percentage
def Calculate_with_percentage(one, two, three):
    Answer = 'Answer: ' + str(round(float(one) / 100 * float(two), int(three))) + '%'
    percent_with_answer.configure(text=Answer)

#calculate with percentage increase
def Calculate_with_percentage_increase(one, two, three):
    onedivided = float(one) / 100
    Answer = 'Answer: ' + str(round(float(two) + onedivided * float(two), int(three))) + '%'
    percent_with_inc_answer.configure(text=Answer)

#calculate with percentage decrease
def Calculate_with_percentage_decrease(one, two, three):
    onedivided = float(one) / 100
    Answer = 'Answer: ' + str(round(float(two) - onedivided * float(two), int(three))) + '%'
    percent_with_dec_answer.configure(text=Answer)

#calculate percentage increase
def Calculate_percentage_increase(one, two, three):
    Answer = 'Answer: ' + str(round(float(one)/float(two)*100, int(three))) + '%'
    percent_inc_answer.configure(text=Answer)

#calculate percentage decrease
def Calculate_percentage_decrease(one, two, three):
    Answer = 'Answer: ' + str(round(float(one)/float(two)*100, int(three))) + '%'
    percent_dec_answer.configure(text=Answer)

def Calculate_percentage_degree_for_pie_chart(one, three):
    Answer = 'Answer: ' + str(round(float(one)/100*360, int(three))) + '%'
    percent_pie_answer.configure(text=Answer)

#topbar
tabview = ctk.CTkTabview(window, width=710, height=410, fg_color='#242424')
tabview.pack(padx=0, pady=0)

tabview.add("Percentages")  # add tab at the end
tabview.add("Triangles")  # add tab at the end
tabview.add("Science")  # add tab at the end

#left bar
tabview = ctk.CTkTabview(tabview.tab("Percentages"), width=700, height=830, fg_color='#2b2b2b')
tabview.pack(padx=0, pady=0)

tabview.add("Calculate percentage")  # add tab at the end
tabview.add("calculate with percentages")  # add tab at the end
tabview.add("Calculate with percentage increase")  # add tab at the end
tabview.add("Calculate with percentage decrease")  # add tab at the end
tabview.add("Calculate percentage increase")  # add tab at the end
tabview.add("Calculate percentage decrease")  # add tab at the end
tabview.add("Calculate percentage degree for pie chart")  # add tab at the end

#percentage

#calculate percentage
percent_cal_val1 =  ctk.CTkEntry(tabview.tab("Calculate percentage"),
                               placeholder_text="How much",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_cal_val1.pack(pady=10)

percent_cal_val2 =  ctk.CTkEntry(tabview.tab("Calculate percentage"),
                               placeholder_text="Total",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_cal_val2.pack(pady=5)

percent_cal_val3 =  ctk.CTkEntry(tabview.tab("Calculate percentage"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_cal_val3.pack(pady=5)

percent_cal_button = ctk.CTkButton(tabview.tab("Calculate percentage"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_percentage(percent_cal_val1.get(), percent_cal_val2.get(), percent_cal_val3.get()))
percent_cal_button.pack(pady=5)

percent_cal_answer = ctk.CTkLabel(tabview.tab("Calculate percentage"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_cal_answer.pack(pady=5)

#calculate with percentage
percent_with_val1 =  ctk.CTkEntry(tabview.tab("calculate with percentages"),
                               placeholder_text="Percent",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_val1.pack(pady=10)

percent_with_val2 =  ctk.CTkEntry(tabview.tab("calculate with percentages"),
                               placeholder_text="Total",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_val2.pack(pady=5)

percent_with_val3 =  ctk.CTkEntry(tabview.tab("calculate with percentages"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_val3.pack(pady=5)

percent_with_button = ctk.CTkButton(tabview.tab("calculate with percentages"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_with_percentage(percent_with_val1.get(), percent_with_val2.get(), percent_with_val3.get()))
percent_with_button.pack(pady=5)

percent_with_answer = ctk.CTkLabel(tabview.tab("calculate with percentages"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_with_answer.pack(pady=5)

#Calculate with percentage increase
percent_with_inc_val1 =  ctk.CTkEntry(tabview.tab("Calculate with percentage increase"),
                               placeholder_text="Percent",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_inc_val1.pack(pady=10)

percent_with_inc_val2 =  ctk.CTkEntry(tabview.tab("Calculate with percentage increase"),
                               placeholder_text="Old Number",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_inc_val2.pack(pady=5)

percent_with_inc_val3 =  ctk.CTkEntry(tabview.tab("Calculate with percentage increase"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_inc_val3.pack(pady=5)

percent_with_inc_button = ctk.CTkButton(tabview.tab("Calculate with percentage increase"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_with_percentage_increase(percent_with_inc_val1.get(), percent_with_inc_val2.get(), percent_with_inc_val3.get()))
percent_with_inc_button.pack(pady=5)

percent_with_inc_answer = ctk.CTkLabel(tabview.tab("Calculate with percentage increase"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_with_inc_answer.pack(pady=5)

#Calculate with percentage decrease
percent_with_dec_val1 =  ctk.CTkEntry(tabview.tab("Calculate with percentage decrease"),
                               placeholder_text="Percent",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_dec_val1.pack(pady=10)

percent_with_dec_val2 =  ctk.CTkEntry(tabview.tab("Calculate with percentage decrease"),
                               placeholder_text="Old Number",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_dec_val2.pack(pady=5)

percent_with_dec_val3 =  ctk.CTkEntry(tabview.tab("Calculate with percentage decrease"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_with_dec_val3.pack(pady=5)

percent_with_dec_button = ctk.CTkButton(tabview.tab("Calculate with percentage decrease"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_with_percentage_decrease(percent_with_dec_val1.get(), percent_with_dec_val2.get(), percent_with_dec_val3.get()))
percent_with_dec_button.pack(pady=5)

percent_with_dec_answer = ctk.CTkLabel(tabview.tab("Calculate with percentage decrease"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_with_dec_answer.pack(pady=5)

#Calculate percentage increase
percent_inc_val1 =  ctk.CTkEntry(tabview.tab("Calculate percentage increase"),
                               placeholder_text="Increase",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_inc_val1.pack(pady=10)

percent_inc_val2 =  ctk.CTkEntry(tabview.tab("Calculate percentage increase"),
                               placeholder_text="Old Number",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_inc_val2.pack(pady=5)

percent_inc_val3 =  ctk.CTkEntry(tabview.tab("Calculate percentage increase"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_inc_val3.pack(pady=5)

percent_inc_button = ctk.CTkButton(tabview.tab("Calculate percentage increase"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_percentage_increase(percent_inc_val1.get(), percent_inc_val2.get(), percent_inc_val3.get()))
percent_inc_button.pack(pady=5)

percent_inc_answer = ctk.CTkLabel(tabview.tab("Calculate percentage increase"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_inc_answer.pack(pady=5)

#Calculate percentage decrease
percent_dec_val1 =  ctk.CTkEntry(tabview.tab("Calculate percentage decrease"),
                               placeholder_text="Decrease",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_dec_val1.pack(pady=10)

percent_dec_val2 =  ctk.CTkEntry(tabview.tab("Calculate percentage decrease"),
                               placeholder_text="Old Number",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_dec_val2.pack(pady=5)

percent_dec_val3 =  ctk.CTkEntry(tabview.tab("Calculate percentage decrease"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_dec_val3.pack(pady=5)

percent_dec_button = ctk.CTkButton(tabview.tab("Calculate percentage decrease"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_percentage_decrease(percent_dec_val1.get(), percent_dec_val2.get(), percent_dec_val3.get()))
percent_dec_button.pack(pady=5)

percent_dec_answer = ctk.CTkLabel(tabview.tab("Calculate percentage decrease"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_dec_answer.pack(pady=5)

#Calculate percentage degree for pie chart
percent_pie_val1 =  ctk.CTkEntry(tabview.tab("Calculate percentage degree for pie chart"),
                               placeholder_text="Percentage",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_pie_val1.pack(pady=10)

percent_pie_val3 =  ctk.CTkEntry(tabview.tab("Calculate percentage degree for pie chart"),
                               placeholder_text="Round",
                               width=150,
                               height=50,
                               border_width=2,
                               corner_radius=30)
percent_pie_val3.pack(pady=5)

percent_pie_button = ctk.CTkButton(tabview.tab("Calculate percentage degree for pie chart"),
                               text="Calculate",
                               width=150,
                               height=50,
                               corner_radius=15,
                               command=lambda: Calculate_percentage_degree_for_pie_chart(percent_pie_val1.get(), percent_pie_val3.get()))
percent_pie_button.pack(pady=5)

percent_pie_answer = ctk.CTkLabel(tabview.tab("Calculate percentage degree for pie chart"),
                               text='Answer: ',
                               font=('Kanit', 25),
                               width=150,
                               height=50,
                               corner_radius=15)
percent_pie_answer.pack(pady=5)

#run
window.mainloop()

# infobar = ctk.CTkFrame(tabview.tab("tab 1"), width=200, height=400, fg_color='#242424')
# infobar.pack(padx=0, pady=0)
