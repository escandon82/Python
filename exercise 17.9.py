# Read Bathing soap and facewash of all months and display it using the Subplot

plt.subplot(2,1,1)
plt.plot("month_number","bathingsoap",data=sales_data,color="black",marker="o")
plt.title("sales data of bathing soap")

plt.subplot(2,1,2)
plt.plot("month_number","facewash",data=sales_data,color="red",marker="o")
plt.xlabel("Month Number")
plt.title("sales data of facewash")
plt.ylabel("sales units in numbers")

plt.subplots_adjust(bottom=0.1,wspace=0.4,hspace=0.3)

plt.show()