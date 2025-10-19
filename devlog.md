# [2025-10-14 6:42pm]
Today, I began actively working on the encryption project implementation using Python.
I first reread the full project description to ensure I understood every requirement in detail.
I confirmed that the project required three programs: a logger, an encryption process, and a driver.
I created a new Git repository to track all future progress and maintain version control.
I added the two provided starter files, cpu.py and mem.py, to study how inter-process communication works.
I executed both scripts together and monitored how data flowed through subprocess pipes.
I observed how flushing output immediately was necessary to avoid blocking between processes.
I tested sending various read and write commands and confirmed the results printed as expected.
I took notes on how the provided example mimics how the driver and the encryption program will interact.
I documented my early observations in the development log for future reference.
I planned to use this foundation as the basis for implementing the logger, encryption, and driver programs.
I outlined the main flow between processes to guide the final implementation phase.
I concluded the day satisfied with a clear roadmap for building the complete system.

# [2025-10-16 8:25pm]
Today, I transitioned from studying the demo code to beginning the real project development.
I started by implementing the logger.py module to handle formatted timestamped logging.
I wrote logic to write log entries using the format YYYY-MM-DD HH:MM [ACTION] MESSAGE.
I tested logger.py by sending sample messages such as START, RESULT, and QUIT manually.
I verified that all entries were written in the correct format with accurate timestamps.
I ensured that the logger properly exited when receiving the QUIT signal.
I then planned the encryption.py file to implement the Vigenère cipher algorithm.
I wrote helper functions for encryption and decryption that work with uppercase-only letters.
I tested those functions with multiple examples to confirm accurate round-trip conversions.
I ensured the encryption program returned the correct RESULT or ERROR responses for every input.
I implemented error handling for cases like missing passwords or invalid characters.
I committed both logger.py and encryption.py to Git with descriptive commit messages.
I closed the day by reviewing the code base and preparing to start the driver program next.

# [2025-03-17 9:10pm]
Today, I implemented the main driver.py file that coordinates the entire project.
I started by configuring driver.py to launch subprocesses for both logger and encryption programs.
I tested process creation using Python’s subprocess module to ensure stable communication.
I built the user interface with commands: password, encrypt, decrypt, history, and quit.
I implemented dynamic history tracking to store all strings entered and generated in one session.
I verified that the password command sets the encryption key correctly for all future operations.
I tested both encrypt and decrypt options thoroughly with known plaintext and ciphertext values.
I confirmed case-insensitive input handling and validation for alphabet-only constraints.
I logged every command and its result using the logger through standard input.
I improved the history display feature for readability and user-friendliness.
I verified that the quit command gracefully shut down both the logger and encryption processes.
I optimized the code for cleaner error messages and smoother user interactions.
I committed driver.py with a clear message describing its functionality and structure.
I ended the day confident that the three essential components were successfully integrated.

# [2025-03-18 7:55pm]
Today, I focused on full-system integration testing and debugging.
I created a dedicated file named mylog.txt to capture real logs during test sessions.
I ran the driver program multiple times to simulate user workflows from start to finish.
I verified that the logger recorded START, RESULT, and EXIT events properly for every command.
I compared the encrypted text against manually calculated Vigenère cipher results for accuracy.
I checked that decrypted messages perfectly matched the original plaintext each time.
I validated that error handling messages appeared correctly in cases of invalid characters.
I tested the history feature by performing several encryption and decryption cycles in sequence.
I confirmed that all session data was correctly maintained and displayed on user request.
I inspected the created log file to ensure timestamps used 24-hour formatting as required.
I tested quitting behavior under various conditions and verified proper termination of processes.
I checked memory usage and ensured that no subprocesses remained active after quitting.
I reflected on how IPC synchronization was stable with no deadlocks or output delays.
I pushed all verified changes to GitHub with detailed commit messages for documentation.
I concluded that the core program now runs consistently and meets all project requirements.

# [2025-03-19 4:46pm]
Today, I finalized the project by refining documentation and preparing for submission.
I wrote a comprehensive README.md that explains the purpose of all three components.
I detailed setup, requirements, and step-by-step instructions for running the driver program.
I added sections describing common errors, testing steps, and expected system behavior.
I included an overview of how inter-process communication is used to connect the programs.
I also added a .gitignore file to keep log files and cache directories out of version control.
I reviewed all previous commits to ensure clarity and accurate chronological order.
I verified that the repository was clean, with only essential Python files and documentation included.
I ran final integration tests using multiple passwords, words, and consecutive operations.
I examined the history and logs to confirm that everything was captured precisely as intended.
I confirmed that the system gracefully terminates under all tested conditions.
I made minor improvements to output formatting for more user-friendly console prints.
I checked documentation formatting to ensure the Markdown rendered clearly on GitHub.
I added this updated development log capturing the entire progress timeline of the project.
I pushed all recent changes, including the README and devlog updates, to the repository.
I created a final backup of the project and reviewed the entire workflow before submitting.
I reflected on how much my understanding of subprocess communication improved through this build.
I ended the session confident that the project is ready for submission and future demonstration.
I closed the log feeling accomplished and proud of the progress achieved throughout development.