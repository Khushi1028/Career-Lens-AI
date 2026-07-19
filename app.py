<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning With Amit</title>
    <style>
        *{ margin:0; padding:0; box-sizing:border-box; font-family: Arial, sans-serif; }
        body{ background:#f5f7fa; }
        header{ background:#003399; color:white; padding:15px 50px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; }
        .logo{ font-size:28px; font-weight:bold; }
        header img{ width:60px; height:60px; border-radius:50%; object-fit:cover; }
        nav ul{ list-style:none; display:flex; }
        nav ul li{ margin-left:25px; }
        nav ul li a{ color:white; text-decoration:none; font-size:18px; }
        .hero{ display:flex; justify-content:space-between; align-items:center; padding:60px; background:white; flex-wrap:wrap; }
        .hero-text{ width:50%; min-width:300px; }
        .hero-text h1{ font-size:50px; color:#003399; }
        .hero-text span{ color:#ff9900; }
        .hero-text p{ margin:20px 0; font-size:20px; color:#333; }
        .btn{ display:inline-block; background:#ff9900; color:white; padding:12px 25px; text-decoration:none; border-radius:5px; }
        .hero img{ width:300px; border-radius:10px; }
        footer{ background:#003399; color:white; text-align:center; padding:20px; margin-top:40px; }
        @media(max-width:768px){ .hero-text{width:100%} header{justify-content:center; gap:15px} }
    </style>
</head>
<body>
    <header>
        <div class="logo">Learning With Amit</div>
        <img src="images/pp2.jpeg" alt="Logo">
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="courses.html">Courses</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>
    <section class="hero">
        <div class="hero-text">
            <h1>Learning <span>With Amit</span></h1>
            <p>Learn Computer, O Level, CCC, Typing, MS Office and many more courses.</p>
            <a href="courses.html" class="btn">Start Learning</a>
        </div>
        <img src="images/pp2.jpeg" alt="Teacher">
    </section>
    <footer>
        <p>© 2026 Learning With Amit | All Rights Reserved</p>
    </footer>
</body>
</html>
