function test {
    param(
        [Parameter(ValueFromPipeline)]
        [string[]]
        $Param1,

        [string]$Param2
    )

    begin {
        Write-Host "Begin"
        Write-Host "firstParam pipeline:" $Param1
        Write-Host "secondParam :" $Param2
    }

    process {
        Write-Host "Process"
        Write-Host "     Первый параметр (через pipeline):" $Param1
        Write-Host "     Второй параметр (аргумент функции):" $Param2
    }

    end {
        Write-Host "End"
        Write-Host "     Первый параметр (через pipeline):" $Param1
        Write-Host "     Второй параметр (аргумент функции):" $Param2
    }
}

'один', 'два', 'три' | test -Param2 'четыре'
