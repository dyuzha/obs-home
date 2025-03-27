
```ps1
Import-Module ActiveDirectory
Import-Module GroupPolicy

Get-ADOrganizationalUnit
# Включает интерактивный определитель OU
Filter: Name -like "krd"
```

```ps1
# Обновить груповые политики на удаленном пк
Invoke-GPUpdate -Computer pc_name
```

```ps1
# Посмотреть список всех gpo
Get-GPO -All | Format-Table GpoStatus,DisplayName
```

```ps1
# Включить/Выключить gpo
$gpo_name = 'Testovaya'

$GPO_DISABLED = "AllSettingsDisabled"
$GPO_ENABLED  = "AllSettingsEnabled"

$gpo = Get-GPO -Name $gpo_name
$gpo.GpoStatus = $GPO_ENABLED
#$gpo.GpoStatus = $GPO_DISABLED

Get-GPO -Name $gpo_name
```
