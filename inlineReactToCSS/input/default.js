export const EVENT_HEIGHT_REM = 5;
export const BUTTON_COLOR = 'salmon';
export const DATE_SELECT_COLOR = 'red';

export const dateSelectStyle = {
    display: 'grid',
    backgroundColor: DATE_SELECT_COLOR,
    gridTemplateColumns: '3rem 4rem 5rem',
    gridTemplateRows: '1fr 3fr',
    gridTemplateAreas: '". . ." ". . ."',
    textAlign: 'center',
    verticalAlign: 'middle',
    gridColumnGap: '1rem',
    padding: '0.5rem 1rem',
    zIndex: '2',
};

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

const optionsContainerStyle = {
    margin: 'auto 4rem',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
};

export const optionsPanelItem = {
    display: 'flex',
    flexWrap: 'wrap',
    padding: '0.5rem 0',
    justifyContent: 'center',
    alignItems: 'center',
};
