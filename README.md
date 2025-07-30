
<h1>Movie Review Sentiment Analyzer 🎬</h1>

<h2>📌 Project Overview</h2>
<p>
This project uses a deep learning model built with TensorFlow to classify movie reviews as positive or negative. 
The model was trained on a dataset of IMDB reviews and can predict the sentiment of any new movie review entered by the user.
The Streamlit app makes it easy to interact with the model through a user-friendly interface.
</p>

<h2>🚀 How to Run Locally (in Google Colab)</h2>
<ol>
  <li>Install Streamlit:</li>
  <pre><code>!pip install streamlit -q</code></pre>

  <li>Check your public IP (optional):</li>
  <pre><code>!wget -q -O - ipv4.icanhazip.com</code></pre>

  <li>Run the Streamlit app and tunnel it using LocalTunnel:</li>
  <pre><code>!streamlit run app.py &amp; npx localtunnel --port 8501</code></pre>
</ol>

<h2>📁 Files in this Repository</h2>
<ul>
  <li><strong>app.py</strong> – Streamlit application file</li>
  <li><strong>sentiment_model.keras</strong> – Trained TensorFlow model in native format</li>
  <li><strong>requirements.txt</strong> – All Python packages needed to run the app</li>
  <li><strong>README.md</strong> – You’re reading it!</li>
</ul>

<h2>✅ Features</h2>
<ul>
  <li>Accepts user input movie reviews</li>
  <li>Predicts and displays sentiment: Positive 😊 or Negative 😞</li>
  <li>Runs seamlessly in Colab with live URL access via LocalTunnel</li>
</ul>

<h2>📌 Notes</h2>
<ul>
  <li>This app is optimized for quick testing and prototyping in Colab.</li>
  <li>To deploy publicly (like on Streamlit Cloud or HuggingFace Spaces), save all files and push this repo to GitHub first.</li>
</ul>

<h2>The UI(Streamlit):</h2>

<img width="944" height="890" alt="image" src="https://github.com/user-attachments/assets/ce95ae02-bb48-4bb3-8c0c-d013593ca22d" />
