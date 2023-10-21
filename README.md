<p class="has-line-data" data-line-start="0" data-line-end="3">KYC-System-for-Fraud-Prevention-and-Identity-Verification<br>
Project Overview<br>
Welcome to the Comprehensive Know Your Customer (KYC) System project! In an era where technology is at the forefront of our daily lives, ensuring the security and authenticity of personal information is of paramount importance. This project aims to create an innovative KYC system that goes beyond traditional identification, diving into the realm of fraud prevention and identity verification through a multi-faceted approach.</p>
<p class="has-line-data" data-line-start="4" data-line-end="6">Project Objectives<br>
The primary objective of this project is to design and implement an efficient KYC system that leverages modern technologies to mitigate the risks associated with identity fraud. The system will offer a comprehensive suite of features to ensure robust identity validation and fraud prevention.</p>
<p class="has-line-data" data-line-start="7" data-line-end="8">Key Components and Features</p>
<ol>
<li class="has-line-data" data-line-start="8" data-line-end="11">
<p class="has-line-data" data-line-start="8" data-line-end="10">Aadhar and PAN Card Verification<br>
The core of our KYC system lies in its ability to accurately compare the data from an individual’s Aadhar and PAN Card documents. Advanced algorithms will ensure that the uploaded documents correspond to the same person, establishing a strong foundation for identity validation.</p>
</li>
<li class="has-line-data" data-line-start="11" data-line-end="14">
<p class="has-line-data" data-line-start="11" data-line-end="13">Multi-Dimensional Verification<br>
Our system will incorporate multi-dimensional verification, cross-referencing personal details such as name, address, and a live raw picture captured through a camera or webcam. This multi-layered approach adds an extra level of security and accuracy, making it difficult for fraudulent individuals to manipulate the system.</p>
</li>
<li class="has-line-data" data-line-start="14" data-line-end="17">
<p class="has-line-data" data-line-start="14" data-line-end="16">Live Camera/Webcam Capture<br>
To enhance the verification process, we have integrated the use of live cameras or webcams. This real-time capture allows the system to compare the live image with the picture on the documents, ensuring the individual undergoing verification is indeed the rightful owner of the documents.</p>
</li>
<li class="has-line-data" data-line-start="17" data-line-end="20">
<p class="has-line-data" data-line-start="17" data-line-end="19">Fraud Prevention<br>
A key goal of our KYC system is proactive fraud prevention. Advanced machine learning techniques enable the system to learn and adapt to new fraudulent patterns, continuously improving accuracy and effectiveness over time.</p>
</li>
<li class="has-line-data" data-line-start="20" data-line-end="23">
<p class="has-line-data" data-line-start="20" data-line-end="22">User-Friendly Interface<br>
We understand the importance of a seamless user experience. The system will be designed with a user-friendly interface, making the KYC process intuitive and easy to navigate. This design approach enhances adoption and acceptance of the system.</p>
</li>
<li class="has-line-data" data-line-start="23" data-line-end="26">
<p class="has-line-data" data-line-start="23" data-line-end="25">Scalability and Integration<br>
Anticipating widespread implementation, our project is designed with scalability and integration in mind. It can be adapted to various platforms and seamlessly integrated into different business models, from financial institutions to e-commerce platforms.</p>
</li>
</ol>
<h2 class="code-line" data-line-start=26 data-line-end=27 ><a id="Installation_26"></a>Installation</h2>
<p class="has-line-data" data-line-start="28" data-line-end="29">To set up and run locally, follow these steps:</p>
<ol>
<li class="has-line-data" data-line-start="30" data-line-end="32"><strong>Clone the Repository</strong>: Clone this repository to your local machine using the following command:<br>
<code>https://github.com/Nitish1206/KYC-System-for-Fraud-Prevention-and-Identity-Verification.git</code></li>
</ol>
<ol start="2">
<li class="has-line-data" data-line-start="34" data-line-end="37">
<p class="has-line-data" data-line-start="34" data-line-end="36"><strong>Create conda environment</strong> : Create anaconda environment using the following command:<br>
<code>conda create --name kyc_auth python=3.8</code></p>
</li>
<li class="has-line-data" data-line-start="37" data-line-end="40">
<p class="has-line-data" data-line-start="37" data-line-end="39"><strong>Activate Environment</strong> : active env<br>
<code>conda activate kyc_auth</code></p>
</li>
<li class="has-line-data" data-line-start="40" data-line-end="50">
<p class="has-line-data" data-line-start="40" data-line-end="49"><strong>Install Dependencies</strong> : Navigate to the project directory and install the required dependencies by running the following command:<br>
<code>pip install tensorflow==2.2.0</code><br>
<code>conda install -c conda-forge dlib=19.23.0</code><br>
<code>pip install flask==2.3.3</code><br>
<code>pip install protobuf==3.19.4</code><br>
<code>pip install opencv-python==4.5.5.64</code><br>
<code>pip install mtcnn==0.1.1</code><br>
<code>pip install easyocr</code><br>
<code>pip install python-dateutil</code></p>
</li>
<li class="has-line-data" data-line-start="50" data-line-end="53">
<p class="has-line-data" data-line-start="50" data-line-end="52"><strong>run application</strong>:<br>
<code>python flask_app.py</code></p>
</li>
</ol>
<p class="has-line-data" data-line-start="53" data-line-end="54">If you encounter the error message “OMP: Error #15: Initializing libiomp5md.dll,” follow these steps to resolve it:</p>
<ul>
<li class="has-line-data" data-line-start="55" data-line-end="57">On Windows, set the environment variable <code>KMP_DUPLICATE_LIB_OK</code> to <code>TRUE</code>.<br>
<code>set KMP_DUPLICATE_LIB_OK=TRUE</code></li>
<li class="has-line-data" data-line-start="57" data-line-end="60">On Linux, export the environment variable <code>KMP_DUPLICATE_LIB_OK</code> as <code>TRUE</code>.<br>
<code>export KMP_DUPLICATE_LIB_OK=TRUE</code></li>
</ul>
<h2 class="code-line" data-line-start=60 data-line-end=61 ><a id="Getting_Started_60"></a>Getting Started</h2>
<p class="has-line-data" data-line-start="62" data-line-end="63">To contribute to this project, follow these steps:</p>
<ol>
<li class="has-line-data" data-line-start="64" data-line-end="65">Clone the repository to your local machine.</li>
<li class="has-line-data" data-line-start="65" data-line-end="66">Set up the necessary development environment (Python, web frameworks, etc.).</li>
<li class="has-line-data" data-line-start="66" data-line-end="67">Explore the project structure and understand the codebase.</li>
<li class="has-line-data" data-line-start="67" data-line-end="69">Familiarize yourself with the project’s goals and key features.</li>
</ol>
<h2 class="code-line" data-line-start=69 data-line-end=70 ><a id="How_to_Use_69"></a>How to Use</h2>
<ol>
<li class="has-line-data" data-line-start="71" data-line-end="72">Run the system on your local machine or deploy it to a server.</li>
<li class="has-line-data" data-line-start="72" data-line-end="73">Navigate to the user-friendly interface via a web browser.</li>
<li class="has-line-data" data-line-start="73" data-line-end="74">Follow the instructions to upload Aadhar and PAN Card documents.</li>
<li class="has-line-data" data-line-start="74" data-line-end="75">Allow the system to capture a live image using your camera or webcam.</li>
<li class="has-line-data" data-line-start="75" data-line-end="76">The system will perform multi-dimensional verification and fraud prevention checks.</li>
<li class="has-line-data" data-line-start="76" data-line-end="78">Receive verification results and feedback in real-time.</li>
</ol>
<h2 class="code-line" data-line-start=78 data-line-end=79 ><a id="Contributions_78"></a>Contributions</h2>
<p class="has-line-data" data-line-start="80" data-line-end="81">We welcome contributions from developers, designers, and anyone interested in enhancing identity verification and fraud prevention systems. To contribute:</p>
<ol>
<li class="has-line-data" data-line-start="82" data-line-end="83">Fork the repository.</li>
<li class="has-line-data" data-line-start="83" data-line-end="84">Create a new branch for your feature or bug fix.</li>
<li class="has-line-data" data-line-start="84" data-line-end="85">Make your changes and commit them.</li>
<li class="has-line-data" data-line-start="85" data-line-end="86">Push your changes to your fork.</li>
<li class="has-line-data" data-line-start="86" data-line-end="88">Open a pull request describing your changes.</li>
</ol>
<h2 class="code-line" data-line-start=88 data-line-end=89 ><a id="Conclusion_88"></a>Conclusion</h2>
<p class="has-line-data" data-line-start="90" data-line-end="91">The Comprehensive KYC System project represents a significant advancement in identity verification and fraud prevention. By integrating modern technology with a multi-dimensional verification approach, we aim to provide a secure and reliable solution to the challenges of our digital age. Join us in creating a safer digital ecosystem for individuals and</p>