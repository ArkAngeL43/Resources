# Native Imports
import os
import argparse


class Hints:
    def __init__(self, name, image):
        self.name = name
        self.image = image
  
    def report_directory(self, name):
        try:
            directory = "./Reports"
            if not os.path.isdir(directory):
                os.makedirs(directory)
            else:
                pass
        except Exception as e:
            print(f"Error encountered...\nReview the following: {str(e)}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="Output name without file extension. Defaults to .html", dest="name")
    parser.add_argument("-i", help="Image of target located in ./Images", dest="image")
    
    args = parser.parse_args()

    InitHints = Hints(args.name, args.image)
    InitHints.report_directory(args.name)
    
    print("\n----------H.I.N.T.S----------")
    print("Human Intelligence Narrowing Tool Set")

    if args != 0:
        
        # Overview
        # --------------------------------------
        _legal_name = input(" Legal name? : ")
        _dob = input(" Date of birth? : ")
        _pronoun = input(" Preferred pronoun? : ")
        _birthplace = input(" Place of birth? : ") 
        _usernames  = input(" Known usernames? : ")
        _nicknames = input(" Known nicknames? : ")
        _emails = input(" Email addresses? : ")
        _phonenumbers = input(" Phone numbers? : ")
        _addresses = input(" Known addresses? : ")
        # Family
        # --------------------------------------
        _contacts = input(" Known contacts? : ")
        _socials = input(" Social media links? : ")
        _familytree = input(" Public family tree information?: ")
        _affiliations = input(" Group Affiliations? : ")
        _trauma = input(" Personal tragedies? : ")
        _relationshipstatus = input(" Relationship status? : ")
        _children = input(" Childrens info? : ")
        _promotions = input(" Recent promotions? : ")
        _health = input(" Public health issues? : ")
        # Electronic Communications
        # --------------------------------------
        _ips = input(" Associated public IP addresses? : ")
        _bluetooth = input(" Bluetooth ID's? : ")
        _ssids = input(" Known SSID's? : ")
        _imeis = input(" Known IMEI's? : ")
        _socialaccounts = input(" Known social footprint? : ")
        _embarrasing = input(" Embarassing data? : ")
        # Assets
        # --------------------------------------
        _income = input(" Estimated yearly income? : ")
        _expenses = input(" Estimated yearly expenses? : ")
        _toi = input(" Standout public transactions? : ")
        _accounts = input(" Public banking information? : ")
        _liabilities = input(" Potential liabilities? : ")
        _taxes = input(" Public tax information? : ")
        _credit = input(" Credit rating? : ")
        _description = input(" Provide a vivid, robust description. : ")
        
        bootstrap =  """<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n
                        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>\n
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\n
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n
                        """

        company = """
                        <header>
                        <div class="pos-f-t">
                            <div class="collapse" id="navbarToggleExternalContent">
                            <div class="bg-dark p-4">
                                <h4 class="text-white">[Company Name]</h4>
                                <span class="text-muted">[Company motto, and other useful information]</span>
                            </div>
                            </div>
                            <nav class="navbar navbar-dark bg-dark">
                            <button class="navbar-toggler" type="button" data-toggle="collapse"
                                data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent"
                                aria-expanded="false" aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                            </button>
                            </nav>
                        </div>

                        <div class="jumbotron jumbotron-fluid">
                        <div class="container">

                    
                            <h1 class="display-4">[Client Name]</h1>
                            <p class="lead">[Scoped name, date of testing, date of completion]</p>
                            
                        </div>
                        </div>
                        </header>
        """

        try:
            setup_report = "./Reports/" + args.name + ".html"
            title_name = args.name
            image_source = args.image
            report = "<!doctype html>\n"
            report += "<html lang='en' ><head>\n"
            report += "<meta charset='utf-8'>\n"
            report += "<meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>\n"
            report += str(bootstrap)
            report += "\n<title>"
            report += str(title_name)
            report += "</title>\n"
            report += "</head>\n"
            report += str(company)
            report += "\n<body>\n"
            # -- Overview begins
            report += "<div class='container'>\n"
            report += "<div class='row justify-content-center'>\n"
            report += "<h1> H.I.N.T.S - Human Intelligence Narrowing Tool Set</h1></div>"
            # Profile Picture
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<img src='../Images/"
            report += str(image_source)
            report += "' class='img-thumbnail mx-auto d-block' alt='Alt_name'>"
            report += "</div></div>\n"
            report += "<br>"
            report += "<hr data-content='H.I.N.T.S' class='solid'>"
            report += "<div class='container'>\n"
            report += "<div class='row justify-content-center'>\n<p>"
            report += str(_description)
            report += "</p></div>"
            report += "<hr data-content='H.I.N.T.S' class='solid'>"
            # Legal Name
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Legal name: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_legal_name)
            report += "</h5></div></div>\n"
            # Date of Birth
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Date of birth: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_dob)
            report += "</h5></div></div>\n"
            # Pronoun
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Pronoun: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_pronoun)
            report += "</h5></div></div>\n"
            # Place of birth
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Place of birth: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_birthplace)
            report += "</h5></div></div>\n"
            # Usernames
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Usernames: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_usernames)
            report += "</h5></div></div>\n"
            # Nicknames
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Nicknames: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_nicknames)
            report += "</h5></div></div>\n"
            # Email Addresses
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Email addresses: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_emails)
            report += "</h5></div></div>\n"
            # Phone Numbers
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Phone numbers: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_phonenumbers)
            report += "</h5></div></div>\n"
            # Addresses
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Addresses: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_addresses)
            report += "</h5></div></div>\n"
            report += "<hr data-content='H.I.N.T.S' class='solid'>"
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Contacts: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_contacts)
            report += "</h5></div></div>\n"
            # Social Media
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Social Media Accounts: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_socials)
            report += "</h5></div></div>\n"
            # Family Tree
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Family tree: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_familytree)
            report += "</h5></div></div>\n"
            # Group Affiliations
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Group affiliations: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_affiliations)
            report += "</h5></div></div>\n"
            # Recent troubles
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Recent troubles: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_trauma)
            report += "</h5></div></div>\n"
            # Relationship status
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Relationship status: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_relationshipstatus)
            report += "</h5></div></div>\n"
            # Children
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Children: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_children)
            report += "</h5></div></div>\n"
            # Recent Promotions
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Recent promotions <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_promotions)
            report += "</h5></div></div>\n"
            # Health issues
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Health issues: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_health)
            report += "</h5></div></div>\n"
            report += "<hr data-content='H.I.N.T.S' class='solid'>"
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>IP addresses: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_ips)
            report += "</h5></div></div>\n"
            # Bluetooth
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Bluetooth ID's: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_bluetooth)
            report += "</h5></div></div>\n"
            # SSID's
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Wifi SSID's: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_ssids)
            report += "</h5></div></div>\n"
            # IMEI's
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Mobile IMEI's: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_imeis)
            report += "</h5></div></div>\n"
            # Social Media Presence
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Social media presence: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_socials)
            report += "</h5></div></div>\n"
            # Embarrasing
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Embarrasing data: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_embarrasing)
            report += "</h5></div></div>\n"
            report += "<hr data-content='H.I.N.T.S' class='solid'>"
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Income data: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_income)
            report += "</h5></div></div>\n"
            # Expenses
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Expenses: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_expenses)
            report += "</h5></div></div>\n"
            # Transactions of interest
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Transactions of interest: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_toi)
            report += "</h5></div></div>\n"
            # Other Accounts
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Other accounts: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_accounts)
            report += "</h5></div></div>\n"
            # Personal liabilities
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Personal liabilities: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_liabilities)
            report += "</h5></div></div>\n"
            # Public tax info
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Public tax information: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_taxes)
            report += "</h5></div></div>\n"
            # Credit rating
            report += "<div class='row justify-content-center'>\n"
            report += "<div class='col'>"
            report += "<h4>Credit score: <h4></div>"
            report += "<div class='col'><h5>"
            report += str(_credit)
            report += "</h5></div></div>\n"
            report += "<hr data-content='H.I.N.T.S' class='solid'>"
            report += "</body></html>"

            report_file = open(setup_report, "w+")
            report_file.write(report)
            report_file.close()
        except Exception as e:
            print(f"Error encountered...\nReview the following: {str(e)}")

        print("Report generated successfull! ")
        print("Take a look in ./Reports. ")
    else:
        print("Damn, back to the drawing board. ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl + C detected, exiting gracefully. ")
    exit(0)