# Journal Setup:
**Title:** KeyDeck  
**Author:** CJ Brandi  
**Description:** A small, 8 switch macropad with 2 leds and a custom case. Has support for macros and shortcuts.  
**Created_at:** 7/28/25  

# Journal Entries:

**Day 1: 7/28/25 - 2 Hours**

Started Initial Creation Process Using The HackPad Tutorial. Modified it slightly when I decided I wanted double the switches. Did very little research in asking ChatGpt if it was possible to use any Gpio pin to wire. Created a basic schematic in the most efficent wiring way possible. Started creating the pcb.

**Day 2: 7/29/30 - 2.5 Hours**

Tried to Finish the pcb for my board according to how I thought it worked and hackpad tutorial. Finished it only to realize it was a terrible layout for the pcb and could've been way more efficent. Noted the pins on the ESP32 and redid everything. Started with doing the schematic correctly, then with my next knowledge and my careful planning, redid the pcb. After redoing it, I added some final branding. After that, I started creating the case based on the board's dimensions. It was hard figuring out where all the holes went, but eventually me and my friend who helped (and was acredited) did it. <img width="1122" height="952" alt="image" src="https://github.com/user-attachments/assets/2a4e698f-7404-4f9b-ba1e-0d0ac9d840f4" /> 
New Schmatic
<img width="1642" height="928" alt="image" src="https://github.com/user-attachments/assets/5c8427f3-3ab2-4da6-9cdb-d06b73dc9c91" />
Case Beta
<img width="1510" height="744" alt="image" src="https://github.com/user-attachments/assets/a7a0cff9-9bb4-40d7-817c-18ed2019a42e" />
Current State of PCB

**Day 3: 7/30/25 - 1.5 Hours**

Pretty Light Day today. I researched some of my parts after reading the requirements for a highway submission. I am still unsure how I am going to get my pcb. I could supply the parts and have it all soldered together for me, I could have the pcb factory source the parts or I could solder them myself. Still unsure how the whole ordering process works. I also added in some screws to the case today to attach the lid. The basic shell for the Keydeck is done but, the final model is not. I can't figure out how to export my pcb as a 3d model properly. I don't even know if I made it correctly. Gonna figure more of that out tomorrow.
<img width="1272" height="794" alt="image" src="https://github.com/user-attachments/assets/b13d069b-2163-46cf-a8fc-38e303a7f6b8" />
Modified Case with Screws
<img width="2662" height="1272" alt="image" src="https://github.com/user-attachments/assets/14d073d9-89af-4e99-8d01-e341f1434887" />
Part Researching
<img width="1318" height="734" alt="image" src="https://github.com/user-attachments/assets/c36b147b-35a7-4355-9216-15726891068c" />
Broken KiCad Step File. Gonna fix tmw hopefully!

**Day 4: 8/2/25 - 1 Hour**

Even though I never got to work on the project on the 31st, i'm now back. Started off today by trying to find out why my pcb cad wasn't fully working. turns out I didn't properly define the edges of my pcb in edge.cuts. fixed it and most of the other errors with my pcb. still some bad things due to the xiao footprint but won't matter because i'm not using the pads by that other cutout. Also worked more on the full cad assembly, specifically after fixing the pcb cad. I researched my parts more and found 3d models for them.  I found a few flaws with my case so I also had help fixing those. Tomorrow, I'm probably gonna make the full assembly and research how I can get the pcb made.
<img width="1082" height="674" alt="image" src="https://github.com/user-attachments/assets/978de042-c044-4484-a680-be1320caa6dc" />
Revamping lid
<img width="1842" height="942" alt="pcb" src="https://github.com/user-attachments/assets/629c4d2a-4d29-43e6-896a-28f6728d7c61" />
fixed pcb.
<img width="1508" height="890" alt="image" src="https://github.com/user-attachments/assets/33f4417d-5e4d-4dd3-9e23-9572ba585201" />
begining of full assembly


**Day 5: 8/3/25 - 3 Hours**

Today was good progress made. I worked on the BOM after reading the highway guidlines for parts. I optimized the parts I picked to be way cheaper, ensuring my projects reliablity and it getting approved quicker do to cheaper overall cost. I also did heavy research on how my project would be assembled and decided against pcb manufactor assembling it because 1, it's way too complicated in how the parts get ther, whether u provide or they source or both and 2, my project doesn't have any super small assemblycomponents so it should be fine to manually do. because I am assmebling myself, I am going to put aside $25 of the budget for soldering supplies as I don't own an iron already. I also completed the cad today (with some more help) and looked into getting it rendered. I know how everything is going to go togther fully now and have something semi-presnetable. 
<img width="1342" height="582" alt="FullCadKeyDeck" src="https://github.com/user-attachments/assets/7638ed0a-c7d0-4046-90c9-c3aa78749a76" />
Full KeyDeck Cad
<img width="2024" height="1238" alt="adafruitleds" src="https://github.com/user-attachments/assets/725aad24-4b9e-432f-95ec-81c2e9de8796" />
led sourcing research
<img width="2564" height="1344" alt="switchesali" src="https://github.com/user-attachments/assets/96d08e0c-4dc7-43ab-b2c7-c73fee3d4dff" />
super cheap switches off aliexpress

**Day 6: 8/4/25 - 1.5 Hours**

Lots of learning going on today as I made my first ever render with blender. I started out not knowing how to use the software at all, but with a little online tutorial help, I made my own render with custom materials! took a lot of trouble shooting but eventually got 3 good enough looking images. 

<img width="831" height="481" alt="Screenshot 2025-08-04 at 10 23 15 PM" src="https://github.com/user-attachments/assets/c0965801-08c7-4646-a1cc-6958697113a0" />
  
Cad Assistant KeyDeck Render

<img width="855" height="533" alt="Screenshot 2025-08-04 at 10 29 40 PM" src="https://github.com/user-attachments/assets/0d0c8b29-f62f-4f3d-bd47-51684bcfc96e" />
  
Blender KeyDeck Step Import

<img width="1019" height="611" alt="Screenshot 2025-08-04 at 10 24 49 PM" src="https://github.com/user-attachments/assets/7f85f35e-ba10-4f6e-8ad0-72fa0ca0fb6f" />
  
ChatGpt render troubleshooting.

<img width="259" height="732" alt="Screenshot 2025-08-04 at 11 28 30 PM" src="https://github.com/user-attachments/assets/b6f5b8ca-9392-4beb-9498-f70f59ae5863" />
  
Me learning how to use blender shader settings


**Day 7: 8/5/25 - 2 Hours**

Everyday now is getting closer and closer to submitting this project. Today, I put on some of the finishing touches of the project such as writing the ReadMe, getting quotes for parts, and creating the BOM. I did some research and made sure that I included all the parts I need to complete the KeyDeck in the BOM. I went to every product I had picked out over the past few days and more that I found today in order to pretend to purchase to get the final cost for each item. I added all of these to an excel BOM file which will be attached with the project. After this, I looked back at the highway website to see what I needed in my readme file. I then began to update that today with project information and lots of images of the preposed KeyDeck. The final step for today was somehow getting my excel workbook into github as a table in my readme. I did some research and found this awesome [website](https://csvtomd.com/#/) that converts csv to markdown tables the github can interpret. I got my excel workbook into a csv and then converted it to the table. Then, I fixed the links because the csv removed them. Also, I uploaded some files today and hopefully the rest tomorrow.

<img width="776" height="1018" alt="pcb_price" src="https://github.com/user-attachments/assets/d163ed0e-afc2-40cb-b042-12f903a0171a" />
  
PCB Final Quote Price
<img width="1812" height="966" alt="solder_iron" src="https://github.com/user-attachments/assets/da8f6674-0a71-4e8f-8957-218697260fe5" />
Soldering Iron Retail Price
<img width="1888" height="1048" alt="KeyDeck_ReadMe_BOM" src="https://github.com/user-attachments/assets/edbd612b-2479-450e-bdb4-a28f986e1d14" />
Finally Fixed BOM Table with WORKING LINKS!!!!

**Day 8: 8/7/25 - 2.5 Hours**

Today is the day!!! After working on this project for about 2 weeks, I am finally submitting it today!!! Today I did some minor things. I uploaded the rest of my missing files to this repo, I reformatted some things in this journal and in my readme, and I created alpha, untested firmware for the KeyDeck. Because the firmware was the last step in creating befor submitting my project, I wasn't sure where to get started. This eventually led me back to the HackPad tutorial. I found out I had 2 options QMK or KMK. I looked into QMK only to find it extremely complicated. Then, I looked into KMK and I was relieved that there was an easier way and solution. I copied the example code from the HackPad page to start and then modified it to my needs for the KeyDeck. The current KeyDeck layout code has every switch print the number switch it is when pressed. the switches are numbered in 2 horizontal rows from left to right. The last thing that I really have to do and I will submit after this is add ti to the gallery. then I get to submit!!!

<img width="2064" height="1300" alt="image" src="https://github.com/user-attachments/assets/e6ecd501-e57f-452e-827a-afac6ddd8f4e" />
  
Me asking ChatGpt about pin correspondance for KMK

<img width="1432" height="578" alt="image" src="https://github.com/user-attachments/assets/0139937f-d90f-47d2-829c-3ceb1d65bb68" />
  
Some of the code I made based on my pcb layout and switch numbering.

<img width="2918" height="632" alt="journaledit" src="https://github.com/user-attachments/assets/b076f4a1-d95b-4e56-908d-38bb1f7b0f74" />
  
Editing my journal to contain the proper header

