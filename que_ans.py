from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os
import speech_recognition as sr
import pyttsx3
from flask import Flask, render_template, request, jsonify
def train_qa():

    bot = ChatBot('ChatBot')
    trainer = ListTrainer(bot)

    trainer.train([
        "Can i Get Address",
        "yup, Gokul Road, Hubballi, Karnataka 580030"

    ])
    trainer.train([
        "can i get contact details",
        "yup, you can contact to this number 155267"
    ])
    trainer.train([
        "can i get Email id",
        "gttcsdchubli@gmail.com"
    ])
    trainer.train([
        "what are Working Hours",
        "Monday to Friday – 10 am to 5pm "

    ])
    trainer.train([
        "What are the facilities available?",
        "Regular classes, \n Certified teachers, \n Sufficient classroom, \n Creative lessons, \n Sports facilities, \n Safety first"
    ])
    trainer.train([
        "available facilities?",
        "Regular classes, \n Certified teachers, \n Sufficient classroom, \n Creative lessons, \n Sports facilities, \n Safety first"
    ])

    trainer.train([
        "what are the special events in campus?",
        "Cultural events, \n Work shops, \n Job fairs,\n Sports events"
    ])

    trainer.train([
        "what are the special events in campus?",
        "Cultural events, \n Work shops, \n Job fairs,\n Sports events"
    ])




    trainer.train([
        "what about placements",
        "From well known companies like Wipro, ORACLE, Zensar Technologies, Quess Corp, Infosys, Xentrix, Informatica, And many more"
    ])

    trainer.train([
        "How about teaching",
        "Teachings at its best with highly qualified staff with certified teachers."
    ])

    trainer.train([
        "Do we get placement assistance training?",
        "yes ofcourse",
    ])





    trainer.train([
        "interview training",
        "yes ofcourse",
    ])



    trainer.train([
        "thanks for guiding me",
        "you are welcome, see you later. have a great day",
    ])

    trainer.train([
        "bye",
        "you are welcome, see you later. have a great day",
    ])





    trainer.train([
        "after completion of the course when i will get my certificate",
        "it may take 1 month for internships and 6 months for free courses",
    ])

    trainer.train([
        "when i will get my certificate",
        "it may take 1 month for internships and 6 months for free courses",
    ])


    trainer.train([
        "internship certificate",
        "it may take 1 month for internships and 6 months for free courses",
    ])

    trainer.train([
        "when i will get my internship certificate",
        "it may take 1 month for internships and 6 months for free courses",
    ])

    trainer.train([
        "is there hostel facility",
        "no",
    ])


    trainer.train([
        "hostel and food",
        "no",
    ])



    trainer.train([
        "any other gttc centers near my place",
        "gttc centers are available in hubli and also in dharwad",
    ])





    trainer.train([
        "gttc centers",
        "gttc centers are available in hubli and also in dharwad",
    ])



    trainer.train([
        "can we pay the course fee by installments",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "installments",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "course fee in installments",
        "ohh sorry,fee need to pay completely at a time",
    ])



    trainer.train([
        "emi",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "any installments available",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "courses installments",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "installment",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "can we pay the fee by installments",
        "ohh sorry,fee need to pay completely at a time",
    ])

    trainer.train([
        "can we get a bus pass",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "can i get bus pass",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "bus pass",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "bus pass for free",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "do i get bus pass",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "free bus pass",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "do i get bus pass instantly",
        "yes, but first you need to pay the application fee, after 3 to 5 days amount will be refunded to your account",
    ])

    trainer.train([
        "what are the courses available for diploma",
        "CAD CAM.,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"
    ])
    trainer.train([
        "courses for diploma",
        "CAD CAM.,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"
    ])
    trainer.train([
        "diploma courses",
        "CAD CAM.,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"
    ])
    trainer.train([
        "diploma",
        "CAD CAM.,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"
    ])
    trainer.train([
        "courses in diploma",
        "CAD CAM.,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    trainer.train([
        "courses available for diploma",
        "CAD CAM.,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"
    ])
    #engineering
    trainer.train([
        "what are the courses available for engineering",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"
    ])
    trainer.train([
        "courses for engineering",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    trainer.train([
        "engineering courses",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    trainer.train([
        "courses for engineering",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    trainer.train([
        "engineering",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    trainer.train([
        "courses in engineering",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    trainer.train([
        "courses available for engineering",
        "CAD CAM,CNC, 3D Printing, IoT, Aerospace CNC,Automation and Robotics, Automobile,Electrical,PCB Design only for electrical branch,solid works"

    ])
    #sslc
    trainer.train([
        "what are the courses available for sslc",
        "aerospace cns,cnc turning,automobile,toyota courses"

    ])
    trainer.train([
        "courses for sslc",
        "aerospace cns,cnc turning,automobile,toyota courses"
    ])
    trainer.train([
        "sslc courses",
        "aerospace cns,cnc turning,automobile,toyota courses"

    ])
    trainer.train([
        "sslc",
        "aerospace cns,cnc turning,automobile,toyota courses"

    ])
    trainer.train([
        "courses in sslc",
        "aerospace cns,cnc turning,automobile,toyota courses"

    ])
    trainer.train([
        "courses for 10th",
        "aerospace cns,cnc turning,automobile,toyota courses"

    ])
    trainer.train([
        "10th courses",
        "aerospace cns,cnc turning,automobile,toyota courses"

    ])
    trainer.train([
        "courses in 10th",
        "aerospace cns,cnc turning,automobile,toyota courses"
    ])
    trainer.train([
        "tenth",
        "aerospace cns,cnc turning,automobile,toyota courses"
    ])
    trainer.train([
        "courses available for sslc",
        "aerospace cns,cnc turning,automobile,toyota courses"
    ])
    trainer.train([
        "courses available for 10th",
        "aerospace cns,cnc turning,automobile,toyota courses"
    ])


    #iti
    trainer.train([
        "what are the courses available for iti",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "courses for iti",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "iti courses",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "iti",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "courses in iti",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "courses available for iti",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])

    #5th

    trainer.train([
        "courses available for 5th",
        "plumbing"
    ])
    trainer.train([
        "5th courses",
        "plumbing"
    ])
    trainer.train([
        "5th",
        "plumbing"
    ])
    trainer.train([
        "courses in 5th",
        "plumbing"
    ])
    trainer.train([
        "fifth",
        "plumbing"
    ])

    trainer.train([
        "courses available for 5th",
        "plumbing"
    ])





    trainer.train([
        "what are the courses available for puc",
        "web development','cloud computing"

    ])
    trainer.train([
        "courses for puc",
        "web development,cloud computing"
    ])
    trainer.train([
        "puc courses",
        "web development,cloud computing"
    ])
    trainer.train([
        "puc",
        "web development,cloud computing"
    ])
    trainer.train([
        "courses in puc"
        "web development,cloud computing"
    ])
    trainer.train([
        "pu",
        "web development,cloud computing"
    ])
    trainer.train([
        "pu courses",
        "web development,cloud computing"
    ])
    trainer.train([
        "12th courses",
        "web development,cloud computing"
    ])
    trainer.train([
        "12th",
        "web development,cloud computing"
    ])
    trainer.train([
        "courses for 12th",
        "web development,cloud computing"
    ])
    trainer.train([
        "courses available for puc",
        "web development,cloud computing"
    ])
    trainer.train([
        "courses available for 12th",
        "web development,cloud computing"
    ])
    trainer.train([
        'what are the courses available for 8th standard'
        'aerospace cns', 'cnc turning', 'automobile', 'toyota courses', 'cnc milling', 'cad cam'
    ])
    trainer.train([
        "courses for 8th"
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "8th courses"
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "courses in 8th"
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])
    trainer.train([
        "eight",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])

    trainer.train([
        "eighth",
        "aerospace cns,cnc turning,automobile,toyota courses,cnc milling,cad cam"
    ])

    #duration
    trainer.train([
        "what is the duration of each course",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])
    trainer.train([
        "course duration",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])
    trainer.train([
        "how many weeks",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])
    trainer.train([
        "how many months",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])
    trainer.train([
        " duration of course",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])
    trainer.train([
        "duration",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])
    trainer.train([
        "what is the maximum duration for free courses",
        "it will be of 2 to 3 months for free courses and 4 weeks for internships"
    ])

    #scheme
    trainer.train([
        "what are the current schemes running",
        "the current scheme is cmkky which means chief minister's kaushalya karnataka yojane"
    ])
    trainer.train([
        " which is the current scheme",
        "the current scheme is cmkky which means chief minister's kaushalya karnataka yojane"
    ])
    trainer.train([
        " scheme",
        "the current scheme is cmkky which means chief minister's kaushalya karnataka yojane"
    ])
    trainer.train([
        "schemes",
        "the current scheme is cmkky which means chief minister's kaushalya karnataka yojane"
    ])
    trainer.train([
        "yojane",
        "the current scheme is cmkky which means chief minister's kaushalya karnataka yojane"
    ])
    # stipend
    trainer.train([
        "do we get stipend",
        "yes, for only sc and st students will get in free courses of two months"
    ])
    trainer.train([
        "stipend",
        "yes, for only sc and st students will get in free courses of two months"
    ])
    trainer.train([
        "how much do we get stipend",
        "yes, for only sc and st students will get in free courses of two months"
    ])
    trainer.train([
        "stipend for students",
        "yes, for only sc and st students will get in free courses of two months"
    ])
    trainer.train([
        "does any stipend available",
        "yes, for only sc and st students will get in free courses of two months"
    ])
    trainer.train([
        "stipend for courses",
        "yes, for only sc and st students will get in free courses of two months"
    ])
    #document
    trainer.train([
        "what are the documents required",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents required",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents for registration",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents for free courses",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents for internships",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "internship documents",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "free courses documents",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents for registering",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    trainer.train([
        "documents for registration",
        "sslc marks card, puc or diploma marks card, caste income certificate,aadhaar card,4 passport size photos"
    ])
    #process
    trainer.train([
        "what is the process to join the course",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "process",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "process to join courses",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "process to join",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "where do i get registration form",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "how to join a course",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "joining process",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    trainer.train([
        "where i get application form",
        "take admission form from the office room which is located at 1st floor and fill it and attach the required documents respectively"
    ])
    #fees
    trainer.train([
        "what is the registration fee for internship",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "internship fees",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "courses fees",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "registration fees",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "fee",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "fees",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "application fee",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "internship fee for engineering",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    trainer.train([
        "internship fee for diploma",
        "for diploma students 2360 rupees only and for engineering students 3540 rupees only"
    ])
    #company
    trainer.train([
        "which are the companies comes for placements?",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "how many companies comes for campus drive",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "companies for placements",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "campus drive companies",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "companies at gttc",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "campus drive",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "placements",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    trainer.train([
        "companies",
        "gttc has tied up with companies like toyota, ptc, sap, autodesk, schneide electric"
    ])
    #internship
    trainer.train([
        "what are the internships available for engineering students",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internship courses",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internships",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internships for engineering",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "engineering internships",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internships available",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internships for students",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internships for degree students",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "what are the internships available for diploma",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internship for diploma",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "diploma internships",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])
    trainer.train([
        "internships available for diploma",
        "ai ml , CAD creo, CAD-solidworks, CAD-NX, Reverse Engineering 3D printing, Advanced manufacturing CNC, CMM, EDN, Robotic programming, web development, python full stack development and Embedded full stack iot, Electrical CAD and Electical Instillation Auto CAD and PCB designing , Iot with thing work , PLC programming "
    ])

    #eligibility
    trainer.train([
        "what is the eligibility for doing internships",
        "the candidate must be cleared diploma atleast 2 years where as for engineering , they have to complete 3 years for doing internships . And age must be within 18 years to 35 years old"
    ])
    trainer.train([
        "eligibility",
        "the candidate must be cleared diploma atleast 2 years where as for engineering , they have to complete 3 years for doing internships . And age must be within 18 years to 35 years old"
    ])
    trainer.train([
        "eligibility for internships",
        "the candidate must be cleared diploma atleast 2 years where as for engineering , they have to complete 3 years for doing internships . And age must be within 18 years to 35 years old"
    ])
    #certificate
    trainer.train([
        "do we get only certificate without attending classes or internships",
        "No, Minimum of 60% attendance must be their to get your internship certificate "
    ])
    trainer.train([
        "without attending classes can we get certificate",
        "No, Minimum of 60% attendance must be their to get your internship certificate "
    ])
    trainer.train([
        "can i get certificate only",
        "No, Minimum of 60% attendance must be their to get your internship certificate "
    ])
    trainer.train([
        "can i get paid certificate",
        "No, Minimum of 60% attendance must be their to get your internship certificate "
    ])
    trainer.train([
        "do i get certificate directly",
        "No, Minimum of 60% attendance must be their to get your internship certificate "
    ])
    trainer.train([
        "instant certificate",
        "No, Minimum of 60% attendance must be their to get your internship certificate "
    ])