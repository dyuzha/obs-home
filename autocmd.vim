

augroup FileType_python
autocmd!
autocmd FileType python :iabbrev <buffer> iff if:<left>
autocmd FileType python nnoremap <buffer> <localleader>c I#<esc>
augroup END

augroup FileType_javascript
autocmd!
autocmd FileType javascript :iabbrev <buffer> iff if ()<left>
autocmd FileType cpp,javascript nnoremap <buffer> <localleader>c I//<esc>
augroup END

augroup FileType_markdown
autocmd FileType markdown inoremap <buffer> < <><esc>i
augroup END

augroup filetype_html
autocmd!
autocmd FileType html nnoremap <buffer> <localleader>f Vatzf
augroup END



