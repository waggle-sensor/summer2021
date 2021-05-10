# Welcome interns!
This guide will give you an overview of how to get started working on the SAGE project.

## Part 1: What is SAGE?
The Sage project's goal is to design and build a new kind of national-scale reusable cyberinfrastructure to enable AI at the edge. To learn about the project, check out the GitHub page, https://github.com/sagecontinuum/sage , and the SAGE project's website, https://sagecontinuum.org/ . I encourage you to explore the SAGE GitHub repository to learn the layout of the project. Be sure to write down any questions you may have while exploring the SAGE GitHub repository. When finished overlooking the repository, contact Raj or Wolfgang regarding questions about the SAGE GitHub repository.

## Part 2: Agile Scrum Development Process
Upon overviewing the repository, the next step is to go over the Agile Scrum framework. Agile Scrum is a workflow that promotes rapid prototyping and efficiency. The SAGE project is following the Agile Scrum develoment process. Every team member is encouraged to watch a six-part video series explaining the Agile Scrum process which can be found in the team's [Agile Scrum Google Drive](https://drive.google.com/drive/folders/1Cj1qPAEVZm1Qkd6BrbIAssERmHlmGf0C). **Download** (to enable document links to work) the latest "Software_Development_Process" PDF and head to section "Agile Scrum Training". The document also contains helpful tutorials on the tools the team uses (i.e. JIRA & Miro). If you have any questions please reach out to Joe Swantek via Slack.

## Part 3: Docker
For the SAGE project, the application [Docker](https://www.docker.com/) is being used extensively. Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Take some time to learn the fundamentals of Docker. Here's a link to a short and friendly tutorial: https://www.youtube.com/watch?v=7S73WERRqO4. Feel free to watch or use any resources to learn about Docker (ex. [https://docs.docker.com/](https://docs.docker.com/)). You will want to have [Docker Desktop](https://www.docker.com/get-started) installed to your computer.

## Part 4: ...
Now that you have finished steps 1-3, report into Raj or Wolfgang. New steps will be added as we figure out what's going on :)



## Part 5: Argonne Server Access Guide

### Account(s) Setup

1. Generate an SSH public key.  
This must be the form of authentication that you use to SSH into any Argonne server. There is a good guide to generating a key [here](https://kb.iu.edu/d/aews).


2. Argonne Collaborator Account  

Skip this if you already have a Argonne Domain or Argonne Collaborator account.

https://apps.anl.gov/registration/collaborators

3. LCRC Account  
Needed to get access to our data store ( https://www.lcrc.anl.gov/for-users/getting-started/getting-an-account/ )

  1. Request membership to the `waggle` project by clicking "Join Project" on the right and then searching for waggle. Also add yourself to the `lcrc` project by doing the same thing. You should automatically be added to `lcrc`, but you will need to contact Raj or Pete when you request access to waggle, since they will need to accept the request.
  2. Add your public SSH key to the LCRC account.


4. JLSE account (Edge Testbed)  
Sage software and hardware will be accessible this summer within an "Edge Testbed", so students and scientists can write AI@Edge code for Sage nodes deployed in the field. Initially, the platforms will be open in "friends and family" mode. We hope to open it up more broadly after we gain some experience with running the Edge Testbed. The initial configuration of the Edge Testbed will be hosted at Argonne through JLSE (thanks Mike!!). Developers and students should sign up for accounts if they do not already have one. These processes take time (particularly for students and mentors who are non-US citizens or PR), so please get started now.

https://accounts.jlse.anl.gov/

All of the above will ask for a few details:

- Sponsor Email: `ozorob@...`
- Reason for the Account: `Write AI@Edge code for Waggle nodes.`

Please feel free to reach out to Omar or Rajesh if you have any further questions.



### SSH Setup

1. .ssh/config  

Add the following configuration to the file `~/.ssh/config` in you home folder on the machine that you will be using to login from: (It the file does not exist, create it.)

   ```text
   Host lcrc
      Hostname bebop.lcrc.anl.gov
      User USERNAME
   ```

   Replace `USERNAME` with your LCRC username. This defines the host `lcrc`.

2. .ssh/rsa_id  

Place your RSA private key (the one that came with your public key) into the `~/.ssh/rsa_id` file. This is where SSH will automatically pull your key from when you login.

3. test ssh  

Run the command `ssh lcrc` to test your ability to log in to Bebop. IMPORTANT: If it asks you for a password in a prompt that looks like `Password:`, you have done something wrong (likely you did not setup an `id_rsa` file correctly). The server should only need your private key, not an additional password. If you try your Argonne password, it will reject it, and in my case, block me from very essential Argonne services.

4. test waggle folder access  

In the Bebop SSH terminal, see if you can access the folder `/lcrc/project/waggle`. If you cannot, Raj or Pete have not accepted your request to join the waggle project on LCRC.
