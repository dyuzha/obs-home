---
id: mikrotik
aliases: []
tags: []
---

```bash
# INPUT chain (правила для трафика, предназначенного самому роутеру):
/ip firewall filter print chain=input

Flags: X - disabled, I - invalid; D - dynamic

 0    ;;; defconf: accept established,related,untracked
      chain=input action=accept connection-state=established,related,untracked

 1    ;;; defconf: drop invalid
      chain=input action=drop connection-state=invalid

 2    ;;; defconf: accept ICMP
      chain=input action=accept protocol=icmp

 3    ;;; defconf: accept to local loopback (for CAPsMAN)
      chain=input action=accept dst-address=127.0.0.1

      # Удалить все что идет не с LAN
 4    ;;; defconf: drop all not coming from LAN
      chain=input action=drop in-interface-list=!LAN


# FORWARD chain (правила для трафика, проходящего через роутер):
Flags: X - disabled, I - invalid; D - dynamic
 0  D ;;; special dummy rule to show fasttrack counters
      chain=forward action=passthrough

 1    ;;; defconf: accept in ipsec policy
      chain=forward action=accept ipsec-policy=in,ipsec

 2    ;;; defconf: accept out ipsec policy
      chain=forward action=accept ipsec-policy=out,ipsec

 3    ;;; defconf: fasttrack
      chain=forward action=fasttrack-connection hw-offload=yes connection-state=established,related

      # Отбрасывать новые соединения без DEST NAT приходящие в Wan
 4    ;;; defconf: drop all from WAN not DSTNATed
      chain=forward action=drop connection-state=new connection-nat-state=!dstnat in-interface-list=WAN
```
