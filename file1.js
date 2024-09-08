* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}





/* General Styles */
body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  color: #333;
}

header {
  background: #4CAF50;
  color: #fff;
  padding: 10px 0;
}

header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

header h1 {
  margin: 0;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

nav ul li {
  margin-left: 20px;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}

nav ul li a:hover {
  text-decoration: underline;
}

.hero {
  background: #f0f8ff;
  padding: 40px 20px;
  text-align: center;
}

.hero h2 {
  margin: 0;
  font-size: 2.5em;
  color: #333;
}

.hero p {
  font-size: 1.2em;
  color: #666;
}

.products {
  padding: 20px;
}

.products h2 {
  text-align: center;
  margin-bottom: 20px;
}

.category-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 10px;
  padding: 15px;
  text-align: center;
  width: 300px;
}

.card img {
  max-width: 100%;
  border-radius: 8px;
}

.card h3 {
  margin-top: 10px;
}

.card p {
  color: #777;
}

.btn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  background: #4CAF50;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
}

.btn:hover {
  background: #45a049;
}

footer {
  background: #333;
  color: #fff;
  padding: 10px 0;
  text-align: center;
}

footer p {
  margin: 5px 0;
}

footer a {
  color: #4CAF50;
  text-decoration: none;
}

footer a:hover {
  text-decoration: underline;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .category-cards {
      flex-direction: column;
      align-items: center;
  }

  .card {
      width: 90%;
  }
}


/* bubble bouncing effect */
.bubble-container {
  position: relative;
  display: inline-block;
  text-align: center;
}

/* Only target h1 inside .bubble-container */
.bubble-container h1 {
  font-size: 36px;
  color: #333;
  margin-top: 20px;
}

.bounceBubble {
  position: absolute;
  top: -50px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #5d9cec;
  color: #fff;
  padding: 10px 20px;
  border-radius: 50px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  font-size: 16px;
  font-weight: bold;
  animation: bounceBubble 2s ease infinite;
}

.bounceBubble::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  border-width: 10px;
  border-style: solid;
  border-color: #5d9cec transparent transparent transparent;
}

/* Keyframes for bounceBubble animation */
@keyframes bounceBubble {
  0%, 20%, 50%, 80%, 100% {
      transform: translateX(-50%) translateY(0);
  }
  40% {
      transform: translateX(-50%) translateY(-20px);
  }
  60% {
      transform: translateX(-50%) translateY(-10px);
  }
