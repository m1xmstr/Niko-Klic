# Episode 130 — Already Done? Ansible Idempotence

**Status:** [Watch the published lesson](https://www.youtube.com/watch?v=r12y_Y8lhTU). Public playback and manual English captions verified October 28, 2026.

**Learning goal:** Run a desired-state directory task twice and compare its change counts. Then request a different directory and repeat.

**Prerequisites:** Episode125 (Ansible YAML) and129 (folders and empty files). A grown-up handles the terminal and setup.

## Story and prediction

Nico types the folder task while Klic helps compare the first and repeated runs. Large terminal panels show the task and its recorded change counts; no program controls physical bins or robots.

The first run creates `art`. Predict: if the same task runs again with the same requested state, does it need to change anything?

**Answer:** No. This task finds the folder already in the requested state. It reports `changed=0`. This repeat-without-extra-change property is called **idempotence**. Not every Ansible task is idempotent.

## Full runnable playbook

Use an empty disposable practice folder on a supported POSIX computer with Ansible installed. Save this as `task.yml` there. The video shows the task excerpt; this is its complete wrapper.

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - ansible.builtin.file:
        path: "{{ playbook_dir }}/art"
        state: directory
        mode: '0700'
```

`playbook_dir` means the directory containing this playbook. The template places `art` inside that practice directory. `state: directory` requests a directory. Quoted mode `'0700'` gives the owner access and no permissions to other users. Use the indentation shown.

Run the same command twice:

```sh
ansible-playbook -i localhost, --limit localhost task.yml
ansible-playbook -i localhost, --limit localhost task.yml
```

The comma makes `localhost,` an explicit one-host inventory. `--limit localhost` further limits this demonstration. No remote hosts, elevated permissions or personal data are needed.

## Actual recorded results

Executed with **ansible-core2.18.5 on macOS**, in a newly created temporary practice folder. All four runs exited0 with `failed=0` and `unreachable=0`.

| Run | Requested folder | Recap |
|---|---|---|
| First | art | `ok=1 changed=1` |
| Repeat, unchanged playbook | art | `ok=1 changed=0` |
| Changed path | music | `ok=1 changed=1` |
| Repeat changed playbook | music | `ok=1 changed=0` |

The on-screen results are concise summaries of these recorded task counts. `changed=1` counts a changed task; it is not a universal count of files created.

## Changed case

Change only `/art` to `/music` in the path:

```yaml
    - ansible.builtin.file:
        path: "{{ playbook_dir }}/music"
        state: directory
        mode: '0700'
```

Save and run the same command twice again. The first run creates `music`; the repeat requires no change. **Both `art` and `music` remain.** Changing this path does not rename or delete `art`. Both directories were verified after execution; the owned temporary fixture was then removed.

## Try it with a grown-up

1. On paper, draw a shelf with one bin labeled `art`. Ask for an `art` bin twice. Check before adding anything.
2. Ask for `music` instead. Add it beside `art`; keep the original.
3. If using a computer, the grown-up creates an empty practice directory, saves the complete localhost playbook, runs the four cases and compares the recap.
4. Check that both folders exist. The grown-up removes only this practice directory afterward.

**Check understanding:** Does `changed=0` mean the command failed? **No:** here it succeeded and found the requested state already satisfied. Check the separate failure count too.

**Transfer question:** What if someone removes `art` between runs? **Answer:** this directory-state task would need to create it again. Idempotence assumes the starting state still matches the request.

[Official Ansible file-module documentation](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/file_module.html) describes directory creation and the task parameters. Our results above come from the actual local execution, not from a simulation.

[Episode library](../README.md)
