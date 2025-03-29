# gemini-ai-bash-assistant
<br> Gemini-AI assistant for automation via bash/python and nice prompt/output in any *nix terminal.
<br>Almost 'headless' installation. With <b>no-selenium</b>, <b>no-chrome-driver</b>, no by-passes or other tricky manipulations.
<br> For complex coding, Gemini offers a clear advantage in accuracy and efficiency, way more excels ChatGPT or DeepSeek.
<br>
<br>This tool has to help with automation, real-time event detection, making it highly effective for log monitoring and system alert generation.
<br>  Requirments:
    Linux;
    FreeBSD;
    Termux;
    Python
    and
    a will to install some python modules.
<br>Usage:
<br> Replace in <b><i>gemini.py</i></b> with your actual API key -> https://aistudio.google.com/app/apikey
<br>
<br>python3 gemini.py -i 'time in Riga'
<br>python3 gemini.py -i 'President of the USA'
<br>python3 gemini.py -i 'meaning of init 1 in linux'
<br>
<br> More *nix <i>way</i> for grep/automation of output monitoring eg. <i>tail -f</i>:
<br>python3 gemini.py -i 'time in Riga' | tee -a gemini.out
<br>python3 gemini.py -i 'President of the USA' | tee -a gemini.out
<br>python3 gemini.py -i 'meaning of init 1 in linux' | tee -a gemini.out
<br>
<br>Uniqness in output file guaranteed by timestamp in seconds of datetime, appended to each AI response.
<br>

<br>p.s. gemini LLM model named <i><b>flash-2.0</b></i> <i>lives</i> in between of October of 2023 and June of 2024 (28 of March, 2025 as per today, as true date).
<br>
<br><b>Automation:</b>
<br>bash gemini-monitor.sh
<br>from another termnal open
<br>python3 gemini.py -post -i 'bash code, create a file, 6 digit time in Riga as filename, file in current folder' | tee -a gemini.out
<br>
<br><b>-post</b> argument passes universal text, of content of file 'post' as appendix for each user prompt to Gemini AI.
<br>
<br>Ubuntu:
<br>![screenshot](1.png)
<br>
<br> Termux (Android mobile phone - Redmi 7):
<br>![screenshot](2.jpg)
<br>
<br> FreeBSD:
<br>![screenshot](3.png)
