soGioLam = float(input("Nhập số giờ làm:"))
luongGio = float(input("Nhập lương trên giờ:"))
gioTieuChuan =  44
gioVuotTieuChuan = max(0, soGioLam - gioTieuChuan)
thucLinh = gioTieuChuan * luongGio + gioVuotTieuChuan * luongGio* 1.5
print(f"số tiền thực lĩnh của nhân viên:{thucLinh}")