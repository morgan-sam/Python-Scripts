const zzwidth = 3;
const zzcolor = '#FF7744';
export const currentTimeMarkerStyle = {
    width: `calc(${EVENT_HEIGHT_REM + 3}rem - 2px)`,
    height: `${zzwidth * 2}px`,
    background: `linear-gradient(-45deg, ${zzcolor} ${zzwidth}px, transparent 0), linear-gradient(45deg, ${zzcolor} ${zzwidth}px, transparent 0)`,
    backgroundSize: `${zzwidth * 2}px ${zzwidth * 2}px`,
    backgroundPosition: 'left-center',
    transformOrigin: `-1px 0%`,
    position: 'absolute',
    top: '0',
    right: '0',
    transform: `rotate(90deg) translateY(-${zzwidth * 2}px)`,
};
