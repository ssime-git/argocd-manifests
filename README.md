# ArgoCD for MLOPS

## K8s usage

1. Install k8s and kubectl
2. create alias for kubectl : 
    > RUN the command `alias k8s='microk8s kubectl'` in the terminal.

## port availability
To check which service is using port 8080, you can use the following command:

```
lsof -i :8080
```

This command will list all the processes that are currently using the specified port (in this case, port 8080).

The output of the command will look similar to the following:

```
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
java     1234 user   41u  IPv4  12345      0t0  TCP 0.0.0.0:8080 (LISTEN)
```

In this example, the process with PID 1234 (a Java application) is listening on port 8080.

If the command doesn't return any output, it means that there is no process currently using port 8080.

You can also use the `netstat` command to achieve the same result:

```
netstat -antp | grep ':8080'
```

This command will list all the active network connections, and you can look for the one that is listening on port 8080.

To link a folder to a Git repository, you can follow these steps:

1. **Open a terminal or command prompt**: Navigate to the folder you want to link to the Git repository.

2. **Initialize a new Git repository**: In the terminal, run the following command to initialize a new Git repository in your folder:

   ```
   git init
   ```

3. **Add the remote repository**: Next, you need to add the URL of the remote Git repository you want to link to. You can get this URL from the hosting service (e.g., GitHub, GitLab, Bitbucket) where your repository is hosted. Run the following command, replacing `<remote_url>` with the actual URL of your remote repository:

   ```
   git remote add origin <remote_url>
   ```

4. **Verify the remote connection**: You can check if the remote repository is correctly linked by running:

   ```
   git remote -v
   ```

   This should display the URL of your remote repository.

5. **Push your local changes**: Now that your folder is linked to the remote Git repository, you can start adding, committing, and pushing your changes. To push your initial commit, run:

   ```
   git add .
   git commit -m "Initial commit"
   git push -u origin master
   ```

   The `-u` option in the `git push` command sets the upstream branch, so you can use `git push` without specifying the remote and branch in the future.

That's it! Your local folder is now linked to the remote Git repository, and you can start managing your project using Git version control.