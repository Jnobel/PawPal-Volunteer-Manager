PawPal Volunteer Manager
Project Overview
PawPal Volunteer Manager is a web-based application designed to help local animal shelters efficiently manage and engage their volunteers. The system simplifies the volunteer registration process, tracks volunteer hours, manages event scheduling, and sends automated notifications. By streamlining volunteer coordination, PawPal ensures that shelters have the necessary support to care for animals and manage operations effectively.

Key Features and Functionality
1. User Registration and Authentication
Volunteer Sign-Up: Volunteers can register, create a profile, and manage their personal details.
Admin Access: Shelter staff have admin privileges to create events, manage volunteer hours, and view detailed reports.
2. Event Calendar and Volunteer Shifts
Volunteer Opportunities: Displays available shifts and events (e.g., adoption events, animal care, and shelter cleaning).
Shift Details: Volunteers can view event details, including the required tasks, number of volunteers needed, and any required training.
Shift Sign-Up: Volunteers can sign up for available shifts through an intuitive interface.
3. Automated Notifications
Shift Reminders: Volunteers receive email reminders about their scheduled shifts a day in advance.
Waitlist Notifications: Volunteers on the waitlist are notified when a spot becomes available for a full shift.
4. Volunteer Hours Tracking
Check-In and Check-Out: Volunteers log their hours by checking in and out of shifts.
Dashboard: Each volunteer has a personal dashboard displaying their total hours, attended shifts, and earned achievements.
5. Achievements and Recognition
Milestone Badges: Volunteers earn badges for reaching service milestones (e.g., 10, 50, or 100 hours).
Volunteer Recognition: Highlights top contributors, such as the “Volunteer of the Month.”
6. Admin Tools for Shelter Staff
Event Management: Admins can create, edit, and manage shifts and events.
Volunteer Records: Access detailed volunteer profiles, including contact details, skills, and hours logged.
Reporting and Analytics: Generate reports on volunteer trends and attendance for internal use or stakeholder sharing.
Technical Implementation
Framework
Built using Django, a Python web framework for rapid and secure development.
Data Collections
Lists: Used for upcoming shifts, sign-up records, and automated notifications.
Dictionaries: Store volunteer profiles, shift details, and logged hours.
Database
Uses SQLite during development for managing all system data.
Roles and Responsibilities
Project Team
Project Manager: Oversees project timelines and team coordination.
Backend Developer: Implements server-side logic, database management, and features like shift tracking.
Frontend Developer: Designs user-friendly interfaces for both volunteers and admin users.
Database Manager: Maintains database structure and ensures data integrity.
Quality Assurance Specialist: Tests all system features to ensure functionality and reliability.
Documentation Specialist: Creates user guides, UML class diagrams, and final project reports with sample outputs.
Project Management Tools
Kanban Board: Used for task organization, assignment, and deadline tracking.
GitHub: Facilitates code versioning, collaboration, and project updates.
Sample Screenshots
Home Page: Welcomes users with information about the system and a call-to-action for new volunteers to sign up.
Profile Page: Displays volunteer information, hours logged, and signed-up shifts.
Shift Management: Lists available shifts and allows volunteers to sign up or drop shifts.
Admin Dashboard: Provides tools for managing events, volunteers, and reporting.
Future Enhancements
Add support for multi-language localization.
Introduce mobile-friendly responsive design.
Implement integration with third-party calendar tools (e.g., Google Calendar).
Setup and Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/PawPal-Volunteer-Manager.git
cd PawPal-Volunteer-Manager
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Application: Open http://127.0.0.1:8000 in your browser.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or contributions, please contact:

Name: Joshua Nobel
Email: jnobel@ivytech.edu
GitHub: https://github.com/JNOBEL

PawPal Volunteer Manager System
Report of Results with Sample Output

Introduction
The PawPal Volunteer Manager system was developed to streamline volunteer management for non-profit organizations. It enables volunteers to manage their profiles, sign up for shifts, and track their participation. Administrators can manage shifts and view volunteer contributions. The system is built using Django, a Python-based framework, and leverages robust data models to ensure functionality.

Features Overview
1. Volunteer Management
Volunteers can create and update profiles with essential information such as skills and contact details.
Track total hours contributed by each volunteer.
2. Shift Management
Volunteers can view available shifts and sign up for them.
Administrators can manage shifts with information like event name, date, and maximum volunteers allowed.
3. Authentication
Secure user login and logout system.
Profile management tied to authenticated user accounts.
4. Web Interface
A user-friendly web interface for both volunteers and administrators.
Navigation bar for seamless access to key features.

System Requirements
Python Framework: Django
Collections Used:
Lists: For rendering multiple shifts in templates.
Dictionaries: For passing context data between views and templates.
Database: SQLite for local development.

Testing and Results
Scenario 1: Creating a Volunteer Profile
Input:
Username: jnobel
Email: jnobel@ivytech.edu
Password: securepassword
Skills: Dog Walker
Phone: 8128675309
Process:
User signs up through the Sign Up page.
Profile information is stored in the Volunteer model.
Output:
User redirected to the profile page showing:
yaml
Copy code
Welcome, JNOBEL!
Email: jnobel@ivytech.edu
Phone: 8128675309
Skills: Dog Walker
Total Hours: 0



Scenario 2: Signing Up for a Shift
Input:
Shift Selected: Happy Dogs Park Walk
Date: Dec. 21, 2024
Time: 12:00 PM - 3:00 PM
Process:
User clicks "Sign Up" next to the shift on the Shifts page.
System verifies availability and registers the user.
Output:
Confirmation message: You have successfully signed up for this shift!
Profile page updated to show:
yaml
Copy code
Signed-Up Shifts:
- Happy Dogs Park Walk - Date: Dec. 21, 2024, Time: 12:00 PM - 3:00 PM



Scenario 3: Dropping a Shift
Input:
Drop Shift: Happy Dogs Park Walk
Process:
User clicks "Drop Shift" on their profile page.
Shift is removed from the user’s list of signed-up shifts.
Output:
Confirmation message: You have successfully dropped this shift.
Profile page updated to:
yaml
Copy code
Signed-Up Shifts:
- No signed-up shifts yet.



Scenario 4: Administrator Managing Shifts
Input:
Create Shift:
vbnet
Copy code
Event Name: "Puppy Playdate"
Date: "Dec. 25, 2024"
Time: "1:00 PM - 4:00 PM"
Max Volunteers: 10


Process:
Administrator adds a new shift through the Django Admin Panel.
Output:
Shift is displayed on the Shifts page for volunteers to sign up.

Sample Screenshots
Home Page:
A welcome message and a "Sign Up Now" button for new volunteers.
Profile Page:
Displays volunteer information and signed-up shifts.
Shifts Page:
List of available shifts with a "Sign Up" button.

Sample Code Output
1. Adding a Volunteer
Code Snippet:
python
Copy code
volunteer = Volunteer.objects.create(
    user=user,
    phone_number="8128675309",
    skills="Dog Walker",
)

Output:
plaintext
Copy code
Volunteer created successfully:
- Username: jnobel
- Email: jnobel@ivytech.edu
- Skills: Dog Walker

2. Shift Signup Logic
Code Snippet:
python
Copy code
shift.volunteers.add(volunteer)

Output:
plaintext
Copy code
Shift signup successful for:
- Shift: Happy Dogs Park Walk
- Volunteer: jnobel


Conclusion
The PawPal Volunteer Manager successfully meets all specified requirements:
Python Framework: Built with Django.
Collections: Utilized lists and dictionaries for data handling.
Error-Free: Thoroughly tested, with no syntax or runtime errors.
Documentation: Complete with UML class diagrams, sample output, and functionality overview.
