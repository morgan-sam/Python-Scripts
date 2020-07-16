export const EVENT_HEIGHT_REM = 5;
export const BUTTON_COLOR = 'salmon';
export const DATE_SELECT_COLOR = 'red';
export const OPTIONS_PADDING = '4rem';
export const DATE_Z_INDEX = 9;
const POINTER_STYLE = 'cursor';
const SPEECH_BOX_COLOR = 'steelblue';
const SPEECH_BOX_WIDTH = '2rem';
const SPEECH_BOX_HEIGHT = '4rem';
const BORDER_COLOR = 'lime';

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
	zIndex: DATE_Z_INDEX
};

export const commonMargin = { margin: '0.5rem', padding: '1rem' };
export const subContainer = { backgroundImage: 'linear-gradient(#fff, #eee)' };
export const parentContainer = { backgroundImage: 'linear-gradient(#fff, #eee)', margin: '1rem' };

export const getBounceButtonStyle = (pressed, delay) => {
	return {
		position: 'relative',
		backgroundImage: 'linear-gradient(#fff, #eee)',
		borderRadius: '1rem',
		cursor: POINTER_STYLE,
		outline: '0',
		lineHeight: '0',
		border: `1px solid ${BORDER_COLOR}`,
		boxShadow: '0 2px 1px #ccc, 0 0.3rem #ccc',
		animation: pressed ? `button-bounce ${delay / 1000}s 1` : 'none'
	};
};

const optionsContainerStyle = {
	margin: 'auto 4rem',
	display: 'flex',
	flexDirection: 'column',
	justifyContent: 'center',
	alignItems: 'center',
	border: `1px solid ${BORDER_COLOR}`
};

export const optionsPanelItem = {
	display: 'flex',
	flexWrap: 'wrap',
	padding: OPTIONS_PADDING,
	justifyContent: 'center',
	alignItems: 'center'
};
