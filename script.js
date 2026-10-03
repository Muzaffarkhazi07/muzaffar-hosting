document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.querySelector(".menu-btn");
    const nav = document.querySelector("nav");

    if (menuBtn && nav) {
        menuBtn.addEventListener("click", () => {
            nav.classList.toggle("active");
        });
    }

    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener("click", function (e) {
            const target = document.querySelector(this.getAttribute("href"));

            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    // Dashboard buttons
    document.querySelectorAll(".btn").forEach(button => {
        button.addEventListener("click", function () {
            const target = this.dataset.target;

            if (target) {
                const section = document.getElementById(target);

                if (section) {
                    section.scrollIntoView({
                        behavior: "smooth"
                    });
                }
            }
        });
    });

    console.log("Hosting Dashboard loaded successfully!");
});
