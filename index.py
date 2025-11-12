from item import Head, Bio, link, Post, Item, Gallery, Tag, award, Moments

head = Head(
    title="Rocky Xu",
    description="Rocky Xu's academic website",
    keywords="Rocky Xu, Ruoqi Xu, Rocky, academic website, personal website",
)

bio = Bio(
    title="Hello, and welcome!",
    image="assets/me.png",
    paragraphs=[
        f"I'm Rocky Xu, a robot engineer 🤖, {link('FIRST', 'https://www.firstinspires.org/robotics/frc')} alumni 🎓 and FRC programming mentor in team {link('8214 Cyber Unicorn', 'https://www.thebluealliance.com/team/8214')} 🦄",
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
            date="2025.07.22",
            description="Champion and autonomous award of FRC 2025 China off-season ",
        ),
        Post(
            date="2025.04.19",
            description="Division finalist and industrial design award of FRC 2025 Houston Championship",
        ),
        Post(
            date="2025.03.16",
            description="Industrial design award of FRC 2025 Shanghai Regional",
        ),
        Post(
            date="2025.03.06",
            description="Autonomous award of FRC 2025 İstanbul Regional",
        ),
    ],
)

_FRC_TAG = Tag(name="FRC", color="0066B3", logo="first")
_FIRST_TAG = Tag(name="FIRST", color="0066B3", logo="first")
_OPENCV_TAG = Tag(name="OpenCV", color="5C3EE8", logo="opencv")
_JAVA_TAG = Tag(name="Java", color="000000", logo="openjdk")
_STM32_TAG = Tag(name="STM32", color="03234B", logo="stmicroelectronics")
_CPP_TAG = Tag(name="C/C++", color="00599C", logo="cplusplus")
_ARDUINO_TAG = Tag(name="Arduino", color="00878F", logo="arduino")

galleries = [
    Gallery(
        name="👔 Employment",
        items=[
            Item(
                image="assets/ni.svg",
                name="NI Robotics",
                tags=[_FIRST_TAG, Tag(name="Education", color="green")],
                links=[
                    "2021.6 - now",
                    link("Email", "mailto:contact@nirobotics.net"),
                    link(
                        "Instagram",
                        "https://www.instagram.com/cyberunicorn8214",
                    ),
                    link(
                        "GitHub",
                        "https://github.com/nirobotics",
                    ),
                ],
                description="CTO",
                bullets=[],
            ),
            Item(
                image="assets/hkclr.png",
                name="HKCLR",
                tags=[Tag(name="CUHK", color="yellow")],
                links=["2023.5 - 2025.10"],
                description="Robotics & Embedded Systems Engineer",
                bullets=[
                    "Developed core programming framework",
                    "Built documentation system",
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
                image="assets/dji.png",
                name="DJI",
                tags=[Tag(name="Unicorn", color="purple")],
                links=["2018.6 - 2018.8"],
                description="Embedded System Intern",
                bullets=[
                    "Developed programming framework",
                ],
                want_negative_film_in_dark_mode=True,
            ),
        ],
    ),
    Gallery(
        name="✨ Project",
        items=[
            Item(
                image="assets/frc_2025_8214.jpg",
                name="FRC 2025 Robot - MANTOU (Team 8214)",
                tags=[
                    _FRC_TAG,
                    _OPENCV_TAG,
                    _JAVA_TAG,
                ],
                links=[
                    award("FRC 2025 China Off-season Champion"),
                    award("FRC 2025 Houston Championship Division Finalist"),
                    "2025.*",
                    link(
                        "NI Robotics STEM Center",
                        "https://github.com/nirobotics",
                    ),
                ],
                description="Competition robot for FRC 2025 - Pipe and ball collection and placement",
                bullets=[
                    "KF-based visual-inertial odometry",
                    "Multi-camera vision system",
                    "OTF path generation with shifted pose",
                    "Full state logging powered by Advantage Kit and Advantage Scope",
                ],
            ),
            Item(
                image="assets/frc_2024_8214.jpg",
                name="FRC 2024 Robot - XiaoBa (Team 8214)",
                tags=[
                    _FRC_TAG,
                    _OPENCV_TAG,
                    _JAVA_TAG,
                ],
                links=[
                    award("FRC 2024 Haliç Regional Champion"),
                    "2024.*",
                    link(
                        "NI Robotics STEM Center",
                        "https://github.com/nirobotics",
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
                    "State-machine based control system",
                ],
            ),
            Item(
                image="assets/frc_2023_8214.png",
                name="FRC 2023 Robot - Vasey (Team 8214)",
                tags=[
                    _FRC_TAG,
                    _OPENCV_TAG,
                    _JAVA_TAG,
                ],
                links=[
                    "2023.*",
                    link(
                        "NI Robotics STEM Center",
                        "https://github.com/nirobotics",
                    ),
                    link(
                        "Robot Reveal", "https://www.bilibili.com/video/BV1so4y1q7DG/"
                    ),
                ],
                description="Competition robot for FRC 2023 - Game piece manipulation",
                bullets=[
                    "UKF-based sensor fusion odometry",
                    "AprilTag-based auto-aiming system",
                    "Hermite spline trajectory generation",
                    "Adaptive Pure Pursuit control",
                    "Model-based joint control with gravity compensation",
                ],
            ),
            Item(
                image="assets/frc_2022_8214.png",
                name="FRC 2022 Robot (Team 8583 & 8214)",
                tags=[
                    _FRC_TAG,
                    _OPENCV_TAG,
                    _JAVA_TAG,
                ],
                links=[
                    award("FRC 2023 China Off-season Champion"),
                    "2022.*",
                    link(
                        "NI Robotics STEM Center",
                        "https://github.com/nirobotics",
                    ),
                    link(
                        "Code",
                        "https://github.com/nirobotics/NI-8214-2022-Public",
                    ),
                ],
                description="Competition robot for FRC 2022 - Ball collection and scoring",
                bullets=[
                    "Multi-sensor fusion odometry (IMU, WO, VO)",
                    "Vision-based auto-aiming",
                    "Hermite spline trajectory generation",
                    "Pure Pursuit trajectory following",
                    "Vision-assisted velocity feedforward aiming control",
                ],
            ),
            Item(
                image="assets/cornerstone.png",
                name="RV CornerStone",
                tags=[
                    _STM32_TAG,
                    _CPP_TAG,
                ],
                links=[
                    "2019.9 - 2021.5",
                    link("RoboVigor", "https://github.com/RoboVigor"),
                    link("Code", "https://github.com/RoboVigor/RV-CornerStone"),
                ],
                description="STM32-based RoboMaster robot framework",
                bullets=[
                    "Modular robot configuration system",
                ],
                want_negative_film_in_dark_mode=True,
            ),
            Item(
                image="assets/dbmal.jpg",
                name="DBMAL",
                tags=[
                    _ARDUINO_TAG,
                    _CPP_TAG,
                ],
                links=[
                    award("Selected work of 2021 International Red Dot Award"),
                    "2021.5",
                    "Chonglang Yuan, Zhirui Zhang, Rocky Xu",
                    link(
                        "Code",
                        "https://github.com/RockyXRQ/DBMAL-Seeeduino",
                    ),
                    link("Video", "https://www.bilibili.com/video/BV1eV4y1g7af"),
                ],
                description="Smart ambient lighting system with audio reactivity",
            ),
        ],
    ),
]
