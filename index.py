from item import Head, Bio, link, Post, Item, Gallery, Tag, award, Moments

head = Head(
    title="Rocky Xu",
    description="Rocky Xu's academic website",
    keywords="Rocky Xu, academic website, personal website",
)

bio = Bio(
    title="Hello, and welcome!",
    image="assets/me.png",
    paragraphs=[
        f"I'm Rocky Xu, a robot engineer 🤖, {link('FIRST','https://www.firstinspires.org/robotics/frc')} alumni 🎓 and FRC programming mentor in team {link('8214 Cyber Unicorn', 'https://www.thebluealliance.com/team/8214')} 🦄",
    ],
    contacts=[
        link("Email", "mailto:rockyxrq@gmail.com"),
        link("Instagram", "https://www.instagram.com/rocky_xrq/"),
        link("Github", "https://github.com/RockyXRQ"),
        link("@Cheryl 💕", "https://www.cheryl-slj.com"),
    ],
)

moments = Moments(
    title="🎉 Moments",
    posts=[
        Post(
            date="2024.03.20",
            description="Champion and industrial design award of FRC 2024 Haliç Regional",
        ),
        Post(
            date="2023.08.06",
            description="Champion and creative award of FRC 2023 China Off-season",
        ),
        Post(
            date="2023.04.02",
            description="Industrial design award of FRC 2023 Smoky Mountain Regional",
        ),
    ],
)

galleries = [
    Gallery(
        name="👔 Employment",
        items=[
            Item(
                image="assets/cartesius.png",
                name="Cartesius Robotics",
                tags=[Tag(name="Startup", color="red")],
                links=["2023.5 - now"],
                description="Software Architect",
                bullets=[
                    "Designed and implemented core system architecture",
                    "Established documentation system and agile development workflow",
                    "Lead product definition and planning",
                ],
            ),
            Item(
                image="assets/hkclr.png",
                name="HKCLR",
                tags=[Tag(name="CUHK", color="yellow")],
                links=["2023.5 - now"],
                description="Robotics & Embedded Systems Engineer",
                bullets=[
                    "Developed core programming framework",
                    "Created technical documentation",
                    "Supported robot design and development",
                ],
            ),
            Item(
                image="assets/siemens.jpg",
                name="SIEMENS",
                tags=[Tag(name="Global 500", color="blue")],
                links=["2022.11 - 2023.5"],
                description="Compliance Intern",
                bullets=[
                    "Automated division workflow processes",
                    "Maintained corporate website",
                    "Obtained Mendix Rapid Developer Certification",
                ],
            ),
            Item(
                image="assets/next_innovation.png",
                name="Next Innovation",
                tags=[Tag(name="Startup", color="red")],
                links=["2021.6 - now"],
                description="Programming Mentor",
                bullets=[
                    "Lead programming for 5 competition robots",
                    "Developed student programming curriculum",
                    "Created team software architecture",
                ],
            ),
            Item(
                image="assets/dji.png",
                name="DJI",
                tags=[Tag(name="Unicorn", color="purple")],
                links=["2018.6 - 2018.8"],
                description="Embedded System Intern",
                bullets=[
                    "Build the programming framework",
                ],
            ),
        ],
    ),
    Gallery(
        name="✨ Project",
        items=[
            Item(
                image="assets/frc_2024_8214.jpg",
                name="FRC 2024 Robot - XiaoBa (Team 8214)",
                tags=[
                    Tag(name="Robotics", color="brightgreen"),
                    Tag(name="Java", color="orange"),
                    Tag(name="OpenCV", color="blue"),
                    Tag(name="Control", color="lightgrey"),
                ],
                links=[
                    award("FRC 2024 Haliç Regional Champion"),
                    "2024.*",
                    link(
                        "Next Innovation STEM Center",
                        "https://github.com/FRCNextInnovation",
                    ),
                    link(
                        "Robot Teaser", "https://www.bilibili.com/video/BV18u4m1A7F3/"
                    ),
                ],
                description="Competition robot for FRC 2024 - Ring collection and scoring",
                bullets=[
                    "UKF-based visual-inertial odometry",
                    "Multi-camera vision system",
                    "Custom trajectory generation with Choreo",
                    "PD-based trajectory tracking",
                    "State machine-based control system",
                ],
            ),
            Item(
                image="assets/frc_2023_8214.jpg",
                name="FRC 2023 Robot - Vasey (Team 8214)",
                tags=[
                    Tag(name="Robotics", color="brightgreen"),
                    Tag(name="Java", color="orange"),
                    Tag(name="OpenCV", color="blue"),
                    Tag(name="Control", color="lightgrey"),
                ],
                links=[
                    "2023.*",
                    link(
                        "Next Innovation STEM Center",
                        "https://github.com/FRCNextInnovation",
                    ),
                    link(
                        "Robot Reveal", "https://www.bilibili.com/video/BV1so4y1q7DG/"
                    ),
                ],
                description="Competition robot for FRC 2023 - Game piece manipulation",
                bullets=[
                    "UKF-based sensor fusion odometry",
                    "AprilTag-based auto-targeting system",
                    "Hermite spline trajectory generation",
                    "Adaptive Pure Pursuit control",
                    "Model-based joint control with gravity compensation",
                ],
            ),
            Item(
                image="assets/frc_2022_8214.jpg",
                name="FRC 2022 Robot (Team 8583 & 8214)",
                tags=[
                    Tag(name="Robotics", color="brightgreen"),
                    Tag(name="Java", color="orange"),
                    Tag(name="OpenCV", color="blue"),
                    Tag(name="Control", color="lightgrey"),
                ],
                links=[
                    award("FRC 2023 China Off-season Champion"),
                    "2022.*",
                    link(
                        "Next Innovation STEM Center",
                        "https://github.com/FRCNextInnovation",
                    ),
                    link(
                        "Robot Code",
                        "https://github.com/FRCNextInnovation/NI-8214-2022-Public",
                    ),
                ],
                description="Competition robot for FRC 2022 - Ball collection and scoring",
                bullets=[
                    "Multi-sensor fusion odometry (IMU, WO, VO)",
                    "Vision-based auto-targeting",
                    "Hermite spline path planning",
                    "Pure Pursuit trajectory following",
                    "Vision-assisted velocity feedforward",
                ],
            ),
            Item(
                image="assets/ni_skeleton.png",
                name="NI Skeleton",
                tags=[
                    Tag(name="System", color="blue"),
                    Tag(name="Robotics", color="brightgreen"),
                    Tag(name="Java", color="orange"),
                    Tag(name="CAN", color="yellow"),
                ],
                links=[
                    "2021.7 - Now",
                    link(
                        "Next Innovation STEM Center",
                        "https://github.com/FRCNextInnovation",
                    ),
                    link(
                        "Github Repo & Doc",
                        "https://github.com/FRCNextInnovation/NI-Skeleton",
                    ),
                ],
                description="High-performance FRC software framework",
                bullets=[
                    "Custom control and driver libraries",
                    "Enhanced WPILIB performance",
                    "Standardized development templates",
                ],
            ),
            Item(
                image="assets/cornerstone.jpg",
                name="RV CornerStone",
                tags=[
                    Tag(name="System", color="blue"),
                    Tag(name="Robotics", color="brightgreen"),
                    Tag(name="STM32", color="grey"),
                    Tag(name="C/C++", color="yellow"),
                    Tag(name="ROS", color="lightgrey"),
                ],
                links=[
                    "2019.9 - 2021.5",
                    link("RoboVigor", "https://github.com/RoboVigor"),
                    link("Github Repo", "https://github.com/RoboVigor/RV-CornerStone"),
                ],
                description="STM32-based RoboMaster robot framework",
                bullets=[
                    "Industry-standard practices",
                    "Modular robot configuration system",
                ],
            ),
            Item(
                image="assets/dbmal.jpg",
                name="DBMAL",
                tags=[
                    Tag(name="Arduino", color="blue"),
                    Tag(name="C/C++", color="yellow"),
                ],
                links=[
                    award(
                        "Selected work of 2021 International Red Dot Concept Design Award"
                    ),
                    "2021.5",
                    "Chonglang Yuan, Zhirui Zhang, Rocky Xu",
                    link(
                        "Github Repo & Doc",
                        "https://github.com/RockyXRQ/DBMAL-Seeeduino",
                    ),
                    link("Video", "https://www.bilibili.com/video/BV1eV4y1g7af"),
                ],
                description="Smart ambient lighting system with audio reactivity",
                bullets=[
                    "HSL-based lighting algorithms",
                    "Touch-controlled mode switching",
                ],
            ),
        ],
    ),
]
