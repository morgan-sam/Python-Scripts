

export const getBounceButtonStyle = (pressed, delay) => {
    return {
        position: 'relative',
        backgroundImage: 'linear-gradient(#fff, #eee)',
        borderRadius: '1rem',
        cursor: 'pointer',
        outline: '0',
        lineHeight: '0',
        border: '1px solid black',
        boxShadow: '0 2px 1px #ccc, 0 0.3rem #ccc',
        animation: pressed ? `button-bounce ${delay / 1000}s 1` : 'none',
    };
};




