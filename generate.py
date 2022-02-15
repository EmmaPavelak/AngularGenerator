import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text, simpledialog
import os
import time
from replacetext import replacetext

# Set home path
homepath = os.path.expanduser(os.getenv('USERPROFILE'))

def generate(project):

    # Angular create
    if project == "create":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/DevTest")

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c ng new " + projectName +
                      " --style=scss --routing --strict")    

            # Gestion 404    
            os.chdir(projectName)   
            os.system("cd src")
            os.system("cmd /c ng g c not-found")

             #remplir not found
            fichier = open("src/app/not-found/not-found.component.html", "w")
            fichier.write("<p>Cette page n'existe pas</p>")
            fichier.close()
        
            #remplir routing-module
            filename = 'src/app/app-routing.module.ts'
            oldtext="const routes: Routes = ["
            newtext= "const routes: Routes = [ { path: 'not-found', component: NotFoundComponent },  { path: '**', redirectTo: 'not-found' }"
            
            replacetext(filename, newtext, oldtext)

             #Ajout des imports
            fileR = open(filename, "r")
            text = fileR.read()
            fileR.close()
            
            textInsert = "import { NotFoundComponent } from './not-found/not-found.component'; \n;"
            
            fileW = open(filename, "w")
            fileW.write(textInsert + text)

            #add form + http modul
            filename = 'src/app/app.module.ts'
            oldtext="imports: ["
            newtext= "imports: [ FormsModule, ReactiveFormsModule,  HttpClientModule,"
            
            replacetext(filename, newtext, oldtext)

            #Ajout des imports
            fileR = open(filename, "r")
            text = fileR.read()
            fileR.close()
            
            textInsert = "import { HttpClientModule } from '@angular/common/http'; \n; import { FormsModule, ReactiveFormsModule } from '@angular/forms'; \n;"
            
            fileW = open(filename, "w")
            fileW.write(textInsert + text)
            
        print(" Creation Done!")          

    # Angular header/footer
    if project == "header":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/DevTest")

        if projectTarget.strip():           
           
            # Aller dans le projet et créer header footer
            os.chdir(projectTarget)        
            os.system("cd src")
            os.system("cmd /c ng g c includes/header")
            os.system("cmd /c ng g c includes/footer")

            #remplir header html
            fichier = open("src/app/includes/header/header.component.html", "w")
            fichier.write("""<header>
            <img
                class="fit-picture"
                src="assets/img/logo.png"
                alt="logo"
            />
            <nav>
                <ul>
                <li>Home</li>
                <li>Contact</li>
                </ul>
            </nav>
            </header>""")
            fichier.close()

            #remplir header style
            fichier = open("src/app/includes/header/header.component.scss", "w")
            fichier.write("""header {
            background-color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            img {
                width: 250px;
                padding: 20px;
            }
            nav {
                ul {
                list-style: none;
                display: flex;
                li {
                    padding: 20px;
                }
                }
            }
            }
            """)
            fichier.close()

            #remplir footer html
            fichier = open("src/app/includes/footer/footer.component.html", "w")
            fichier.write("""<footer>
            <div>{{title}} © {{ currentYear }} - Tous droits réservés</div>
            </footer>""")
            fichier.close()

            #remplir footer style
            fichier = open("src/app/includes/footer/footer.component.scss", "w")
            fichier.write("""footer {
                background-color: grey;
                color: #fff;
                text-align: center;
                padding: 10px;
                }
                """)
            fichier.close()

            #remplir footer component
            fichier = open("src/app/includes/footer/footer.component.ts", "w")
            fichier.write("""import { Component, OnInit } from '@angular/core';
            @Component({
            selector: 'app-footer',
            templateUrl: './footer.component.html',
            styleUrls: ['./footer.component.scss'],
            })
            export class FooterComponent implements OnInit {
            currentYear = new Date().getFullYear();

            constructor() {}

            ngOnInit(): void {}
            }
                """)
            fichier.close()



            #remplir app component
            fichier = open("src/app/app.component.html", "w")
            fichier.write("<app-header></app-header><router-outlet></router-outlet><app-footer></app-footer>")
            fichier.close()

            print(" Header/Footer Done!")

    # Angular login
    if project == "login":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/DevTest")

        if projectTarget.strip():           
           
            # Aller dans le projet et créer signin signup
            os.chdir(projectTarget)        
            os.system("cd src")
            os.system("cmd /c ng g c auth/sign-in")
            os.system("cmd /c ng g c auth/sign-up")

            #remplir sign-in
            with open(homepath + "/Downloads/Program-Generator-master/files/sign-in.html", "r") as fichier1, open("src/app/auth/sign-in/sign-in.component.html", "w") as fichier2:
                for ligne in fichier1:
                    fichier2.write(ligne)

            #remplir sign-up
            with open(homepath + "/Downloads/Program-Generator-master/files/sign-up.html", "r") as fichier1, open("src/app/auth/sign-up/sign-up.component.html", "w") as fichier2:
                for ligne in fichier1:
                        fichier2.write(ligne)          

            #remplir sign-up style
            fichier = open("src/app/auth/sign-up/sign-up.component.scss", "w")
            fichier.write("footer{text-align:center;}")
            fichier.close()

            #remplir routing-module
            filename = 'src/app/app-routing.module.ts'
            oldtext="const routes: Routes = ["
            newtext= "const routes: Routes = [{ path: 'sign-in', component: SignInComponent }, { path: 'sign-up', component: SignUpComponent },"
            
            replacetext(filename, newtext, oldtext)

            #Ajout des imports
            fileR = open(filename, "r")
            text = fileR.read()
            fileR.close()
            
            textInsert = "import { SignInComponent } from './auth/sign-in/sign-in.component';\n import { SignUpComponent } from './auth/sign-up/sign-up.component'\n;"
            
            fileW = open(filename, "w")
            fileW.write(textInsert + text)

            print("SignUp/SignIn Done !")

    # Angular CRUD
    if project == "crud":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/DevTest")

        if projectTarget.strip():
            # Set project name
            crudName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your CRUD ? ")

            # Generate crud component
            os.chdir(projectTarget)       
            os.system("cd src")
            os.system("cmd /c ng g c "+ crudName)
            os.system("cmd /c ng g s services/"+ crudName +" --skipTests ")
            os.system("cmd /c ng g interface models/"+ crudName )

            #remplir service
            with open(homepath + "/Downloads/Program-Generator-master/files/crud-service.txt", "r") as fichier1, open("src/app/services/"+crudName+".service.ts", "w") as fichier2:
                for ligne in fichier1:
                    fichier2.write(ligne.replace("products",crudName.lower()))

            #remplacer les elements en capitalize
            with open("src/app/services/"+crudName+".service.ts", "rt") as file:
                x = file.read()
                
            with open("src/app/services/"+crudName+".service.ts", "wt") as file:
                x = x.replace("Product",crudName.capitalize())
                file.write(x)   

            #remplir component
            with open(homepath + "/Downloads/Program-Generator-master/files/crud-component.txt", "r") as fichier1, open("src/app/"+crudName+"/"+crudName+".component.ts", "w") as fichier2:
                for ligne in fichier1:
                    fichier2.write(ligne.replace("product",crudName.lower()))

            #remplacer les elements en capitalize
            with open("src/app/"+crudName+"/"+crudName+".component.ts", "rt") as file:
                x = file.read()
                
            with open("src/app/"+crudName+"/"+crudName+".component.ts", "wt") as file:
                x = x.replace("Product",crudName.capitalize())
                file.write(x)   

            #remplir html
            with open(homepath + "/Downloads/Program-Generator-master/files/crud.html", "r") as fichier1, open("src/app/"+crudName+"/"+crudName+".component.html", "w") as fichier2:
                for ligne in fichier1:
                    fichier2.write(ligne.replace("product",crudName.lower()))            

            #remplir routing-module
            filename = 'src/app/app-routing.module.ts'
            oldtext="const routes: Routes = ["
            newtext= "const routes: Routes = [{ path: '"+crudName.lower()+"', component:" +crudName.capitalize()+"Component },"
            
            replacetext(filename, newtext, oldtext)

            #Ajout des imports
            fileR = open(filename, "r")
            text = fileR.read()
            fileR.close()
            
            textInsert = "import { "+crudName.capitalize()+"Component} from './"+crudName.lower()+"/"+crudName.lower()+".component'; \n;"
            
            fileW = open(filename, "w")
            fileW.write(textInsert + text)

             #add service dans provider
            filename = 'src/app/app.module.ts'
            oldtext="providers: ["
            newtext= "providers: [ "+crudName.capitalize()+"Service,"
            
            replacetext(filename, newtext, oldtext)

            #Ajout des imports
            fileR = open(filename, "r")
            text = fileR.read()
            fileR.close()
            
            textInsert = "import { "+crudName.capitalize()+"Service } from './services/"+crudName.lower()+".service'; \n;"
            
            fileW = open(filename, "w")
            fileW.write(textInsert + text)
            

            print("CRUD "+ crudName + " Done !")

    # Open project in explorer
   # os.system("cmd /c start " + projectTarget + "/" + projectName)
