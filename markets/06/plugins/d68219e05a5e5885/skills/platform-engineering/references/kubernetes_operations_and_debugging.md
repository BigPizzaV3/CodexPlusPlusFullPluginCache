# Kubernetes Operations and Debugging

## Diagnostic path

`declaration → admission → scheduler → kubelet/runtime → container startup → readiness → service/endpoints → ingress/gateway → dependency`

Find the first failing boundary.

## Useful evidence

When available:
- `kubectl get ... -o wide`
- `kubectl describe`
- events ordered by time;
- pod/container status and termination reason;
- current/previous logs;
- rollout status/history;
- endpoints / EndpointSlices;
- node conditions;
- metrics;
- network/DNS evidence.

Do not ask for every command at once. Request the smallest evidence that separates likely causes.

## Pending pod

Check:
- scheduler events;
- resource requests;
- affinity/anti-affinity;
- taints/tolerations;
- topology constraints;
- PVC binding;
- node selectors;
- quotas.

Do not add nodes until the actual scheduling reason is known.

## CrashLoopBackOff

Check:
- last termination reason/exit code;
- previous logs;
- startup command;
- config/secrets;
- probes;
- OOM;
- dependency failure.

A restart can hide evidence; preserve logs/reason first.

## Readiness failure

A readiness failure removes the pod from service traffic.

Check:
- endpoint semantics;
- app startup;
- dependencies that truly determine readiness;
- timeout/threshold;
- port/path;
- network policy.

Do not put every external dependency into liveness.

## Liveness failure

Liveness should answer whether restarting the container can restore progress.

A bad liveness probe can create restart loops and amplify outages.

## OOMKilled / throttling

Check:
- requests/limits;
- actual working set;
- spikes;
- concurrency;
- GC/runtime behavior;
- leaks;
- node pressure.

Do not solve every OOM by only increasing the limit.

## Service unreachable

Check:
- selector;
- endpoints;
- readiness;
- service port / targetPort;
- DNS;
- network policy;
- ingress/gateway;
- application bind address.

## Rollout stuck

Check:
- new ReplicaSet;
- image/tag/digest;
- probes;
- quota/capacity;
- PDB;
- strategy;
- progress deadline;
- dependency/config changes.

## PDB nuance

PodDisruptionBudgets limit voluntary disruptions.

They do not protect against:
- node crash;
- pod crash;
- every involuntary disruption;
- bad application rollouts.

Use them with sufficient replicas/topology and safe maintenance workflows.

## Recovery

Contain with:
- rollback to known-good;
- pause rollout;
- route traffic away;
- scale only when evidence supports capacity need;
- disable a faulty feature via existing safe mechanism.

Then fix root cause and add a regression signal.
