import { remToPx } from 'utility/convertUnit';

export const GRAPH_SIZES = {
	TOP_GAP: remToPx(5),
	BOTTOM_GAP: remToPx(5),
	LEFT_GAP: remToPx(5),
	RIGHT_GAP: remToPx(3),
	FONT_SIZE: remToPx(1)
};

export const formStyle = {
	display: 'flex',
	flexDirection: 'column',
	alignItems: 'center',
	justifyContent: 'center'
};

export const formInputStyle = {
	margin: '0.6rem 0'
};
