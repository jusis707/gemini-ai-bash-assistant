# gemini-ai-bash-assistant
<br> Gemini-AI assistant for automation via bash/python and nice prompt/output in any *nix terminal.
<br>Almost 'headless' near 'lazy' installation. With <b>no-selenium</b>, <b>no-chrome-driver</b>, no by-passes or other tricky manipulations.
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
<br>git clone https://github.com/jusis707/gemini-ai-bash-assistant
<br>cd gemini-ai-bash-assistant
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
<br><i> - from terminal:</i>
<br>bash gemini-monitor.sh
<br><i> - from another terminal open:</i>
<br>python3 gemini.py -post -i 'bash code, create a file, 6 digit time in Riga as filename, file in current folder' | tee -a gemini.out
<br>
<br><b>-post</b> argument passes universal text, of content of file 'post' as appendix for each user prompt to Gemini AI.
<br>
<br><b>gemini-monitor.sh</b> runs in background (optionally, might use '&' or 'nohup') to keep <i>backgrounded</i> and monitors Gemini AI responses - if any code responded, then the code executes and actions will be appended to logfile.
<br>
<br>Reminder:
<br>  If:
<br>  <b>-post</b> argument added
<br>and
<br>  <b>bash gemini-monitor.sh</b> started, then:
<br>  <b>Gemini AI responded <i>code</i> WILL execute.</b>
<br>
<br>Ubuntu .deb file added, for easy/lazy installation:
<br><b>sudo dpkg -i ./gemini-agent_0.1.0-1_amd64.deb</b> API key asked during installation and saved in <b>config.ini</b> file.
<br>Ubuntu deb package installation:
<br>![screenshot](4.png)
<br>Ubuntu version with deb file installation runs with:
<br><b>gemini -i 'time in riga'</b>
<br> note the difference between Ubuntu direct run <i>gemini</i> and python way of <i>python3 gemini.py</i>
<br>
<br>Ubuntu:
<br>![screenshot](1.png)
<br>
<br> Termux (Android mobile phone - Redmi 7):
<br>![screenshot](2.jpg)
<br>
<br> FreeBSD:
<br>![screenshot](3.png)
