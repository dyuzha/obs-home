function test {
  param(
    [parameter(ValueFromPipeline)]
    [string[]]
    $Param1,

    [string]$Param2
  )

  begin {
    Write-Host "begin: " $Param1
    Write-Host "begin: " $Param2
  }

  process {
    Write-Host "proc: " $Param1
    Write-Host "proc: " $Param2
  }

  end {
    Write-Host "End"
    Write-Host "pipeline: " $Param1
    Write-Host "arg: " $Param2
    }
}

'1', '2', '3' | test -Param2 '4'
